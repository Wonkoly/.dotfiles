from libqtile.config import Screen
from widgets import widgets
from libqtile import bar
from theme import colors, bar_size
from bar_toggle import DEFAULT_BAR_VISIBILITY, bar_states

# Create a screen with a bottom bar and initialise its visibility according to
# the global state stored in ``bar_states``. The same approach can be extended to
# multiple screens if needed.
screens = [Screen(bottom=bar.Bar(widgets, bar_size, background=colors["background"]))]

for i, screen in enumerate(screens):
    bar_states.setdefault(i, DEFAULT_BAR_VISIBILITY)
    if not bar_states[i]:
        screen.bottom.show(False)
