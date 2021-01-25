import socket
import sys

from app_config import AppMetaInfo
from utils.log_utils import logger

_AUTH_STR = "xadl "


def _encode_message(msg):
    msg = _AUTH_STR + msg
    return msg.encode()


class UnixDomainClient:
    def __init__(self):
        self.server_address = "/var/tmp/xadl-audit"
        self._sock_fd = None
        self._connect()

    def _connect(self):
        self._sock_fd = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        logger.debug('connecting to {}'.format(self.server_address))
        try:
            self._sock_fd.connect(self.server_address)
        except socket.error as ex:
            logger.exception("can not connect to {}".format(self.server_address), exc_info=ex)
            sys.exit(1)

    def invoke_service_run(self, msg) -> bool:
        try:
            logger.info('invoke {}'.format(msg))
            self._sock_fd.sendall(_encode_message(msg))
            return True
        except Exception as ex:
            logger.exception("send {} error".format(msg), exc_info=ex)
            return False
        finally:
            self._sock_fd.close()

