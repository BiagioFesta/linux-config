import env
import i3
import os
import polybar
import traceback
import utilities.system
import rofi
import gtk
import picom
import alacritty
import redshift


MODULES = [
    {
        'name': 'env',
        'module': env
    },
    {
        'name': 'i3',
        'module': i3
    },
    {
        'name': 'polybar',
        'module': polybar
    },
    {
        'name': 'rofi',
        'module': rofi
    },
    {
        'name': 'gtk',
        'module': gtk
    },
    {
        'name': 'picom',
        'module': picom
    },
    {
        'name': 'alacritty',
        'module': alacritty
    },
    {
        'name': 'redshift',
        'module': redshift
    }]

def _install() -> bool:
    for module in MODULES:
        module_name = module['name']
        module = module['module']

        try:
            print("Installing '{}' module...".format(module_name))
            module.install()

        except Exception as err:
            print('\n' + traceback.format_exc())
            print("\n!!ERROR: {}".format(err))
            ans = input("Error during installation of module '{}'. You wanna ABORT? [Yn]: "
                        .format(module_name))
            if ans != 'n' and ans != 'N':
                print("  Process aborted with errors")
                return False

    return True

def _check():
    for module in MODULES:
        module_name = module['name']
        module = module['module']

        print("Checking '{}' module...".format(module_name))
        module.check();

    # Additional checks
    for binary in ['pavucontrol',
                   'pulseaudio',
                   'cargo',
                   'rustup',
                   'rustc']:
        utilities.system.check_binary(binary)


def _main():
    _install()
    _check()


if __name__ == '__main__':
    _main()
