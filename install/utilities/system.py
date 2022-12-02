import subprocess
import sys
import re
import os
import utilities.fs


def is_linux() -> bool:
    return sys.platform == "linux" or sys.platform == "linux2"


def is_bin(binary: str) -> bool:
    if not is_linux():
        print("Cannot check '{}' binary: not linux platform"
              .format(binary))
        return False

    ans = subprocess.run(["which", binary], capture_output=True, check=False)
    return ans.returncode == 0


def check_binary(binary: str):
    if not is_bin(binary):
        print("[WARN]: binary '{}' seems to not be installed on the system"
              .format(binary))


def check_font(font: str):
    if not is_linux():
        print("[WARN]: Cannot check '{}' font: not linux platform"
              .format(font))
        return

    if not is_bin('fc-list'):
        print("[WARN]: Cannot check '{}' font: 'fc-list' cmd not installed"
              .format(font))
        return

    output = subprocess.run(["fc-list"], capture_output=True, check=True)
    stdout = output.stdout.decode('utf-8')
    for line in stdout.split('\n'):
        m = re.match(r'([^:]*)\s*:\s*([^:]*)\s*:.*', line)
        if m:
            names = [n.strip() for n in m.group(2).split(',')]
            for n in names:
                if n == font:
                    return

    print("[WARN]: font '{}' seems to not be installed on the system"
          .format(font))


def check_icon_theme(theme: str):
    if not is_linux():
        print("[WARN]: Cannot check '{}' icon theme. Not linux platform"
              .format(theme))
        return

    FONTS_DIR = ['/usr/share/icons',
                 '~/.local/share/icons']

    for font_dir in FONTS_DIR:
        if utilities.fs.is_path_exists(font_dir, prefix_home=False):
            for item in os.listdir(font_dir):
                filepath = os.path.join(font_dir, item)
                if os.path.isdir(filepath) and item == theme:
                    return

    print("[WARN]: Icon theme '{}' seems to not be installed on the system"
          .format(theme))


def check_theme(theme: str):
    if not is_linux():
        print("[WARN]: Cannot check '{}' theme. Not linux platform"
              .format(theme))
        return

    THEMES_DIR = ['/usr/share/themes',
                  '~/.themes']

    for theme_dir in THEMES_DIR:
        if utilities.fs.is_path_exists(theme_dir, prefix_home=False):
            for item in os.listdir(theme_dir):
                filepath = os.path.join(theme_dir, item)
                if os.path.isdir(filepath) and item == theme:
                    return

    print("[WARN]: Theme '{}' seems to not be installed on the system"
          .format(theme))


def check_systemd_unit(unit_name: str, check_enabled: bool = False):
    if not is_linux():
        print("[WARN]: Cannot check '{}' systemd unit. Not linux platform"
              .format(unit_name))
        return

    ans = subprocess.run(["systemctl", "--user", "cat", unit_name],
                         capture_output=True,
                         check=False)

    if ans.returncode != 0:
        print("[WARN]: Systemd unit file '{}' seems to not be installed on"
              " the system"
              .format(unit_name))
        return

    if check_enabled == False:
        return

    ans = subprocess.run(["systemctl", "--user", "status", unit_name],
                         capture_output=True,
                         check=False)

    output = ans.stdout.decode('utf-8').splitlines()
    if len(output) < 3:
        print("[WARN]: Cannot parse systemd unit file '{}' status".format(unit_name))
        return

    loaded = output[1].strip()
    active = output[2].strip()

    m = re.match(r"Loaded: loaded \(.*; (.*); preset: (.*)\)", loaded)
    if m is None:
        print("[WARN]: Cannot parse systemd unit file '{}' status/loaded".format(unit_name))
    elif m.group(1) != 'enabled':
        print("[WARN]: It seems systemd unit file '{}' is not enabled".format(unit_name))

    m = re.match(r"Active: ([^\s]*)\s.*", active)
    if m is None:
        print("[WARN]: Cannot parse systemd unit file '{}' status/active".format(unit_name))
    elif m.group(1) != 'active':
        print("[WARN]: It seems systemd unit file '{}' is not active".format(unit_name))
