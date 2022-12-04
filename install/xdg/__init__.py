import utilities.fs
import utilities.system


XDG_DEFAULTS_LIST = '.local/share/applications/defaults.list'


def install():
    utilities.fs.create_symlink('xdg/defaults.list', XDG_DEFAULTS_LIST)


def check():
    utilities.fs.check_file(XDG_DEFAULTS_LIST)

    utilities.system.check_binary('nsxiv')
