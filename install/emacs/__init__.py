import utilities.fs
import utilities.system
import os


EMACS_SERVICE_FILE=os.path.join(utilities.fs.SYSTEMD_SERVICE_UNIT_DIR, 'emacs.service')


def install():
    utilities.fs.create_dir(utilities.fs.SYSTEMD_SERVICE_UNIT_DIR)
    utilities.fs.create_symlink('emacs/emacs.service', EMACS_SERVICE_FILE)



def check():
    utilities.system.check_binary('emacs')

    utilities.fs.check_path(utilities.fs.SYSTEMD_SERVICE_UNIT_DIR)
    utilities.fs.check_file(EMACS_SERVICE_FILE)
    utilities.system.check_systemd_unit('emacs', check_enabled=True)
