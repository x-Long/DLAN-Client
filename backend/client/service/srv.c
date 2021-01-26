// ref: https://github.com/troydhanson/network/tree/master/unixdomain/01.basic
#include <syslog.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/un.h>
#include <stdlib.h>
#include <errno.h>

const char* sock_path = "/var/tmp/xadl-audit";


int run_commands(const char* fcmd) {
    const char* auth_str = "xadl ";
    const int auth_len = strlen(auth_str);

    if (strncmp(fcmd, auth_str, auth_len)) {
        fprintf(stderr, "invalid sender\n%s\n", fcmd);
        return -1;
    }
    const char* cmd = fcmd + auth_len;
    printf("[*] %s\n", cmd);
    FILE* fp;
    if ((fp = popen(cmd, "r")) == NULL) {
        printf("Error opening pipe!\n");
        return -1;
    }

    char buf[512];
    while (fgets(buf, sizeof buf, fp) != NULL) {
        syslog(LOG_NOTICE, "%s", buf);
    }

    return pclose(fp);
}

void process_client_request(const int fd) {
    char in_buf[1024];
    char out_buf[8];
    int in_len = 0;
    while ((in_len=read(fd, in_buf, sizeof(in_buf)-1)) > 0) {
        in_buf[in_len] = '\0';
        int status_code = run_commands(in_buf);

        memset(out_buf, 0, sizeof out_buf);
        int len = snprintf(out_buf, sizeof out_buf, "%d", status_code);
        write(fd, out_buf, len);
    }
    if (in_len == -1) {
        perror("read");
    }
    else if (in_len == 0) {
        close(fd);
    }
}

void server_loop(int listen_sock) {
    while (1) {
        int client_fd = 0;
        if ((client_fd = accept(listen_sock, NULL, NULL)) > 0) {
            process_client_request(client_fd);
        } else {
            perror("accept error");
        }
    }
}

int setup_server() {
    struct sockaddr_un addr;
    int fd;
    if ( (fd = socket(AF_UNIX, SOCK_STREAM, 0)) == -1) {
        perror("socket error");
        exit(-1);
    }

    memset(&addr, 0, sizeof(addr));
    addr.sun_family = AF_UNIX;
    strncpy(addr.sun_path, sock_path, sizeof(addr.sun_path)-1);
    unlink(sock_path);

    if (bind(fd, (struct sockaddr*)&addr, sizeof(addr)) == -1) {
        perror("bind error");
        return -1;
    }

    if (listen(fd, 5) == -1) {
        perror("listen error");
        return -1;
    }
    return fd;
}

int main(int argc, char *argv[]) {
    // enable none root user connect
    umask(S_IXOTH);
    
    int fd = setup_server();
    if (fd < 0) {
        exit(-1);
    }

    server_loop(fd);

    return 0;
}
