from subprocess import check_output

from utils.system_utils import OSUtils


def get_latest_version_from_tag() -> str:
    # return like this 2.2.0.1
    cmd = "git for-each-ref --sort=creatordate refs/tags"
    output = check_output(cmd, shell=True).strip()
    # output like this
    # 1851605c6d8a25d16da15ec4995e291ff1d7bea3 tag	refs/tags/release-1.1.0.1
    output = output.decode()
    version = output.split('-')[-1]
    assert len(version) > 0
    assert version.count('.') == 3
    return version


def get_latest_commit() -> str:
    cmd = "git rev-parse master"
    output = check_output(cmd, shell=True).strip().decode()
    # output like this
    # 272b5649505b7d988c08c84c4a487e5424727782
    commit = output[:8]
    return commit


def generate_next_build_version():
    current_tag_version = get_latest_version_from_tag()
    last_dot = current_tag_version.rfind('.')
    main_version = current_tag_version[:last_dot]
    build_version = current_tag_version[last_dot+1:]
    assert build_version.isdigit()
    new_build_version = int(build_version) + 1
    new_tag = "{}.{}".format(main_version, new_build_version)
    return new_tag


def generate_next_build_tag() -> str:
    next_build_version = generate_next_build_version()
    tag_prefix = "release"
    next_build_tag = "{}-{}".format(tag_prefix, next_build_version)
    return next_build_tag


def make_next_build_tag():
    new_tag = generate_next_build_tag()
    cmd = "git tag {}".format(new_tag)
    print("set new tag", new_tag)
    OSUtils.shell_run(cmd)


if __name__ == '__main__':
    make_next_build_tag()
