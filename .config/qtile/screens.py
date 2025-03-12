from libqtile.config import Screen
from widgets import widgets
from libqtile import bar
from theme import colors

screens = [
    Screen(top=bar.Bar(widgets, 26, background=colors["background"])),
]

