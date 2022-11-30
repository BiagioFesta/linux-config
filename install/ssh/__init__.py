import utilities.system
import utilities.fs
import os


SYSTEMD_SERVICE_UNIT_DIR = '.config/systemd/user'


def install():
    utilities.fs.create_dir(SYSTEMD_SERVICE_UNIT_DIR)
    utilities.fs.create_symlink('ssh/ssh-agent.service',
                                os.path.join(SYSTEMD_SERVICE_UNIT_DIR, 'ssh-agent.service'))


def check():
    utilities.fs.check_path(SYSTEMD_SERVICE_UNIT_DIR)
    utilities.system.check_binary('ssh-agent')
    utilities.system.check_systemd_unit('ssh-agent')
