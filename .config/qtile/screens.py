from libqtile.config import Screen
from widgets import widgets
from libqtile import bar
from theme import colors, bar_size

show_bar = True  # Esta variable puede ser modificada dinámicamente

if show_bar:
    screens = [Screen(bottom=bar.Bar(widgets, bar_size, background=colors["background"]))]
else:
    screens = [Screen()]
