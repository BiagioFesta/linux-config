import utilities.system
import utilities.fs
import os


ROFI_CONFIG_DIR = '.config/rofi'
ROFI_CONFIG = os.path.join(ROFI_CONFIG_DIR, 'config.rasi')
NORD_CONFIG = os.path.join(ROFI_CONFIG_DIR, 'nord.rasi')


def install():
    utilities.fs.create_dir(ROFI_CONFIG_DIR)
    utilities.fs.create_symlink('rofi/config.rasi', ROFI_CONFIG)
    utilities.fs.create_symlink('rofi/nord.rasi', NORD_CONFIG)


def check():
    utilities.system.check_binary('rofi')

    utilities.system.check_font('Source Code Pro')

    utilities.system.check_icon_theme('Papirus-Dark')

    utilities.fs.check_file(ROFI_CONFIG)
    utilities.fs.check_file(NORD_CONFIG)
