import utilities.system
import utilities.fs
import os


PICOM_CONFIG_DIR = '.config/picom'
PICOM_CONFIG = os.path.join(PICOM_CONFIG_DIR, 'picom.conf')


def install():
    utilities.fs.create_dir(PICOM_CONFIG_DIR)
    utilities.fs.create_symlink('picom/picom.conf', PICOM_CONFIG)


def check():
    utilities.system.check_binary('picom')

    utilities.fs.check_file(PICOM_CONFIG)
