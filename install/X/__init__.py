import utilities.fs

XRESOURCES_CONFIG_FILE = '.Xresources'


def install():
    utilities.fs.create_symlink('X/Xresources', XRESOURCES_CONFIG_FILE)


def check():
    utilities.fs.check_file(XRESOURCES_CONFIG_FILE)
