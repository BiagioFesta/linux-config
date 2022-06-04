import utilities.system
import utilities.fs
import os
import subprocess
import re

I3_CONFIG_DIR = '.config/i3'
I3_CONFIG = os.path.join(I3_CONFIG_DIR, 'config')
WALLPAPERS_DIR = '.wallpapers'
I3_ADDS_CONFIG_DIR = os.path.join(I3_CONFIG_DIR, 'config.d')


def install():
    utilities.fs.create_dir(I3_CONFIG_DIR)
    utilities.fs.create_symlink('i3/config', I3_CONFIG)

    utilities.fs.create_dir(WALLPAPERS_DIR)
    utilities.fs.create_symlink('i3/wg1.jpg',
                                os.path.join(WALLPAPERS_DIR, 'wg1.jpg'))
    utilities.fs.create_symlink('i3/wg2.png',
                                os.path.join(WALLPAPERS_DIR, 'wg2.png'))

    utilities.fs.create_symlink('i3/startup_icon.svg',
                                os.path.join(I3_CONFIG_DIR,
                                             'startup_icon.svg'))

    utilities.fs.create_dir(I3_ADDS_CONFIG_DIR)


def check():
    utilities.system.check_binary('i3')
    utilities.system.check_binary('feh')
    utilities.system.check_binary('setxkbmap')
    utilities.system.check_binary('xset')
    utilities.system.check_binary('picom')
    utilities.system.check_binary('emacs')
    utilities.system.check_binary('rofi')
    utilities.system.check_binary('alacritty')
    utilities.system.check_binary('polybar')
    utilities.system.check_binary('nm-applet')
    utilities.system.check_binary('pasystray')
    utilities.system.check_binary('redshift')
    utilities.system.check_binary('redshift-gtk')
    utilities.system.check_binary('pactl')
    utilities.system.check_binary('brightnessctl')
    utilities.system.check_binary('notify-send')
    utilities.system.check_binary('dunst')
    utilities.system.check_binary('dunstctl')

    utilities.fs.check_file(I3_CONFIG)
    utilities.fs.check_file(os.path.join(WALLPAPERS_DIR, 'wg1.jpg'))
    utilities.fs.check_file(os.path.join(WALLPAPERS_DIR, 'wg2.png'))
    utilities.fs.check_file(os.path.join(I3_CONFIG_DIR, 'startup_icon.svg'))

    utilities.fs.check_path(I3_ADDS_CONFIG_DIR)

    _check_i3_version()


def _check_i3_version():
    ans = subprocess.run(["i3", "--version"], capture_output=True, check=True)
    stdout = ans.stdout.decode('utf-8')
    m = re.search(r'version ((\d+)\.(\d+)\.(\d+))', stdout)
    if m:
        version = m.group(1)
        major = int(m.group(2))
        minor = int(m.group(3))

        if major >= 4 and minor >= 20:
            return

        print("[WARN]: i3 detected version ('{}') does not support 'include' "
              "directive. Required >= i3 v4.20".format(version))

    else:
        raise Exception("Cannot detect the version of i3 '{}'".format(stdout))
