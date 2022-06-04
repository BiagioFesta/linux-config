import utilities.fs
import utilities.system
import os


GTK3_CONFIG_DIR='.config/gtk-3.0'
GTK3_CONFIG=os.path.join(GTK3_CONFIG_DIR, 'settings.ini')


def install():
    utilities.fs.create_dir(GTK3_CONFIG_DIR)
    utilities.fs.create_symlink('gtk/3/settings.ini', GTK3_CONFIG)


def check():
    utilities.fs.check_file(GTK3_CONFIG)

    utilities.system.check_font('Source Code Pro')

    utilities.system.check_icon_theme('Papirus-Dark')

    utilities.system.check_theme('Orchis')
