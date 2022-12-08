import utilities.system
import utilities.fs
import os


SSH_CONFIG = '.ssh/config'


def install():
    utilities.fs.create_dir(utilities.fs.SYSTEMD_SERVICE_UNIT_DIR)
    utilities.fs.create_symlink('ssh/ssh-agent.service',
                                os.path.join(utilities.fs.SYSTEMD_SERVICE_UNIT_DIR, 'ssh-agent.service'))


def check():
    utilities.fs.check_path(utilities.fs.SYSTEMD_SERVICE_UNIT_DIR)
    utilities.system.check_binary('ssh-agent')
    utilities.system.check_systemd_unit('ssh-agent', check_enabled=True)

    utilities.fs.check_file(SSH_CONFIG)
    if utilities.fs.is_file_exists(SSH_CONFIG):
        if not utilities.fs.lookup_line(SSH_CONFIG, 'AddKeysToAgent yes'):
            print("[WARN]: 'AddKeysToAgent yes' is missing in ssh config")
