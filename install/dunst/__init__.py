import utilities.system
import utilities.fs
import os


DUNST_CONFIG_DIR = '.config/dunst/'
DUNST_CONFIG = os.path.join(DUNST_CONFIG_DIR, 'dunstrc')


def install():
    utilities.fs.create_dir(DUNST_CONFIG_DIR)
    utilities.fs.create_symlink('dunst/dunstrc', DUNST_CONFIG)


def check():
    utilities.fs.check_file(DUNST_CONFIG)

    utilities.system.check_binary('dunst')
    utilities.system.check_font('Source Code Pro')
    utilities.system.check_icon_theme('Papirus-Dark')
