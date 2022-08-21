import utilities.fs
import utilities.system
import os


def _append_line_if_not_yet(filename: str,
                            line: str,
                            prefix_home: bool = True) -> bool:
    filename = os.path.join(utilities.fs.home_dir(), filename) \
        if prefix_home else filename

    utilities.fs.ensure_file(filename, prefix_home=False)

    if not utilities.fs.lookup_line(filename, line, prefix_home=False):
        with open(filename, 'a') as f:
            f.write(line)
        return True

    return False


def install():
    utilities.fs.create_dir(".env")
    utilities.fs.create_dir(".env/profile.d")
    utilities.fs.create_dir(".env/bashrc.d")

    utilities.fs.create_symlink("env/profile", ".env/profile")
    utilities.fs.create_symlink("env/bashrc", ".env/bashrc")

    if _append_line_if_not_yet('.profile',
                               '\nsource "${HOME}/.env/profile"\n'):
        print("Source profile")

    if _append_line_if_not_yet('.bashrc',
                               '\nsource "${HOME}/.env/bashrc"\n'):
        print("Source bashrc")


def check():
    for f in ['.profile',
              '.bashrc',
              '.env/profile',
              '.env/bashrc']:
        utilities.fs.check_file(f)

    for f in ['.bash_profile', 'bash_login']:
        if utilities.fs.is_file_exists(f):
            print("The file '{}' should not exist".format(f))

    utilities.system.check_binary('alacritty')
    utilities.system.check_binary('neofetch')
    utilities.system.check_binary('fzf')

    utilities.fs.check_file(".fzf.bash")
