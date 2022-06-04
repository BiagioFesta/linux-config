import utilities.system
import utilities.fs
import os


POLYBAR_CONFIG_DIR = '.config/polybar'
POLYBAR_CONFIG = os.path.join(POLYBAR_CONFIG_DIR, 'config.ini')
POLYBAR_LAUNCHER = os.path.join(POLYBAR_CONFIG_DIR, 'polybar-restart.sh')


def install():
    utilities.fs.create_dir(POLYBAR_CONFIG_DIR)
    utilities.fs.create_symlink('polybar/config.ini', POLYBAR_CONFIG)
    utilities.fs.create_symlink('polybar/polybar-restart.sh', POLYBAR_LAUNCHER)


def check():
    utilities.system.check_binary('polybar')
    utilities.system.check_binary('polybar-msg')
    utilities.system.check_binary('dunstctl')

    utilities.fs.check_file(POLYBAR_CONFIG)
    utilities.fs.check_file(POLYBAR_LAUNCHER)

    utilities.system.check_font('Source Code Pro')
    utilities.system.check_font('Font Awesome 5 Free')
    utilities.system.check_font('Iosevka Nerd Font')

    if not utilities.fs.is_path_exists('/sys/class/power_supply/BAT0',
                                       prefix_home=False):
        print("[WARN]: '/sys/class/power_supply/BAT0' not found. "
              "Probably polybar battery module will not work")

    if not utilities.fs.is_path_exists('/sys/class/backlight/intel_backlight',
                                       prefix_home=False):
        print("[WARN]: '/sys/class/backlight/intel_backlight' not found. "
              "Probably polybar backlight module will not work")
