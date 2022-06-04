import os
import re
import pathlib

def home_dir() -> str:
    return os.environ['HOME']


def repo_dir() -> str:
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(this_dir, "../.."))


def is_path_exists(filepath: str, prefix_home: bool = True) -> bool:
    filepath = os.path.join(home_dir(), filepath) if prefix_home else filepath
    return os.path.isdir(filepath)


def is_file_exists(filename: str, prefix_home: bool = True) -> bool:
    filename = os.path.join(home_dir(), filename) if prefix_home else filename
    return os.path.isfile(filename)


def create_dir(directory: str, force_override: bool = True, prefix_home: bool = True):
    directory = os.path.join(home_dir(), directory) if prefix_home else directory

    print("Creating directory '{}'".format(directory))

    if is_path_exists(directory, prefix_home = False):
        print("  Directory '{}' already exists".format(directory))

        if force_override == True:
            print("  (ignore override)")
            return

        ans = input("  The directory '{}' already exists. You wanna CONTINUE? [yN]: "
                    .format(directory))
        if ans != 'y' and ans != 'Y':
            raise Exception("The directory '{}' already exists".format(directory))
        else:
            return

    os.makedirs(directory)


def create_symlink(src: str, dest: str, prefix_repo: bool = True, prefix_home: bool = True):
    src = os.path.join(repo_dir(), src) if prefix_repo else src
    dest = os.path.join(home_dir(), dest) if prefix_home else dest

    print("Creating symlink '{}' -> '{}'".format(src, dest))

    if not is_file_exists(src, prefix_home = False):
        raise Exception("The file to install ('{}') does not exist".format(src))

    if is_file_exists(dest, prefix_home = False):
        ans = input("  Destination ('{}') already exists. You wanna OVERRIDE? [yN]: "
                    .format(dest))
        if ans != 'y' and ans != 'Y':
            return

        delete_file(dest, prefix_home = False)

    if not is_path_exists(os.path.dirname(dest), prefix_home=False):
        raise Exception("The directory where to install ('{}/') does not exist"
                        .format(os.path.dirname(dest)))

    os.symlink(src, dest)


def delete_file(filename, prefix_home: bool = True):
    filename = os.path.join(home_dir(), filename) if prefix_home else filename

    if is_path_exists(filename, prefix_home = False):
        raise Exception("Trying to delete '{}', but it is a directory!"
                        .fornmat(filename))

    print("Deleting file '{}'".format(filename))

    os.remove(filename)


def create_file(filename: str, prefix_home: bool = True):
    filename = os.path.join(home_dir(), filename) if prefix_home else filename

    print("Creating file '{}'".format(filename))

    assert(not is_file_exists(filename, prefix_home = False))

    f = open(filename, "x")
    f.close()


def ensure_file(filename: str, prefix_home: bool = True):
    filename = os.path.join(home_dir(), filename) if prefix_home else filename

    if not is_file_exists(filename, prefix_home = False):
        print("The file '{}' does not exist. I am gonna create it".format(filename))
        create_file(filename, prefix_home = False)


def lookup_line(filename: str, pattern: str, prefix_home: bool = True):
    filename = os.path.join(home_dir(), filename) if prefix_home else filename
    pattern = pattern.strip()

    assert(is_file_exists(filename, prefix_home = False))

    with open(filename, 'r') as f:
        for line in f:
            if pattern in line:
                return True

    return False


def check_file(filename: str, prefix_home: bool = True):
    filename = os.path.join(home_dir(), filename) if prefix_home else filename

    if not is_file_exists(filename, prefix_home = False):
        print("[WARN]: required file '{}' does not exist".format(filename))
