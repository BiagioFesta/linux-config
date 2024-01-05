import utilities.system
import utilities.fs
import os


ALACRITTY_CONFIG_DIR = '.config/alacritty'
ALACRITTY_CONFIG = os.path.join(ALACRITTY_CONFIG_DIR, 'alacritty.toml')


def install():
    utilities.fs.create_dir(ALACRITTY_CONFIG_DIR)
    utilities.fs.create_symlink('alacritty/alacritty.toml', ALACRITTY_CONFIG)


def check():
    utilities.system.check_binary('alacritty')
    utilities.system.check_font('Source Code Pro')
    utilities.fs.check_file(ALACRITTY_CONFIG)
