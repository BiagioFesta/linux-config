import utilities.fs
import utilities.system


RANGER_RIFLE_CONFIG= '.config/ranger/rifle.conf'


def install():
    utilities.fs.create_symlink('ranger/rifle.conf', RANGER_RIFLE_CONFIG)


def check():
    utilities.fs.check_file(RANGER_RIFLE_CONFIG)

    utilities.system.check_binary('ranger')
    utilities.system.check_binary('xdg-open')
