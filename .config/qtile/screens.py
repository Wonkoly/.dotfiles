from libqtile.config import Screen
from widgets import widgets
from libqtile import bar
from theme import colors

show_bar = True  # Esta variable puede ser modificada dinámicamente

if show_bar:
    screens = [Screen(top=bar.Bar(widgets, 26, background=colors["background"]))]
else:
    screens = [Screen()]
