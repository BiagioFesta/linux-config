import utilities.system
import utilities.fs
import os


REDSHIFT_CONFIG_DIR = '.config/redshift'
REDSHIFT_CONFIG = os.path.join(REDSHIFT_CONFIG_DIR, 'redshift.conf')


def install():
    utilities.fs.create_dir(REDSHIFT_CONFIG_DIR)
    utilities.fs.create_symlink('redshift/redshift.conf', REDSHIFT_CONFIG)


def check():
    utilities.system.check_binary('redshift')
    utilities.system.check_binary('redshift-gtk')

    utilities.fs.check_file(REDSHIFT_CONFIG)
