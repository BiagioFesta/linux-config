import utilities.system
import utilities.fs
import os

I3_CONFIG_DIR='.config/i3'
I3_CONFIG=os.path.join(I3_CONFIG_DIR, 'config')
WALLPAPERS_DIR='.wallpapers'


def install():
    utilities.fs.create_dir(I3_CONFIG_DIR)
    utilities.fs.create_symlink('i3/config', I3_CONFIG)

    utilities.fs.create_dir(WALLPAPERS_DIR)
    utilities.fs.create_symlink('i3/wg1.jpg', os.path.join(WALLPAPERS_DIR, 'wg1.jpg'))
    utilities.fs.create_symlink('i3/wg2.png', os.path.join(WALLPAPERS_DIR, 'wg2.png'))

    utilities.fs.create_symlink('i3/startup_icon.svg', os.path.join(I3_CONFIG_DIR, 'startup_icon.svg'))


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

    utilities.fs.check_file(I3_CONFIG)
    utilities.fs.check_file(os.path.join(WALLPAPERS_DIR, 'wg1.jpg'))
    utilities.fs.check_file(os.path.join(WALLPAPERS_DIR, 'wg2.png'))
    utilities.fs.check_file(os.path.join(I3_CONFIG_DIR, 'startup_icon.svg'))
