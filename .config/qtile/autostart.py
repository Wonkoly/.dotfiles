import os
import subprocess


COMMANDS = [
    ["picom", "--config", os.path.expanduser("~/.config/picom/picom.conf")],
    ["brightnessctl", "set", "50%"],
    ["feh", "--bg-scale", os.path.expanduser("~/Images/soul-eater1.jpg")],
    ["nm-applet"],
    ["blueman-applet"],
    ["volumeicon"],
    ["dunst"],
    ["cbatticon"],
    ["xset", "r", "rate", "300", "50"],
    ["kitty"],
    ["firefox"],
    ["/home/cokie/Applications/Todoist.AppImage"],
    ["spotify-launcher"],
]


def run():
    """Launch autostart applications."""
    for cmd in COMMANDS:
        subprocess.Popen(cmd)

