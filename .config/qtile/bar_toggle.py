"""Utilities to toggle the visibility of Qtile bars.

`bar_states` stores the current visibility of each screen's bar. The
`DEFAULT_BAR_VISIBILITY` flag defines the initial visibility for any screen
that does not yet have an entry in ``bar_states``.
"""

from libqtile import qtile

# Default visibility for newly discovered bars. ``True`` means the bar starts
# visible.
DEFAULT_BAR_VISIBILITY = True

# Keeps track of the visibility state of each bar. Keys are screen indexes and
# values are booleans indicating whether the bar is currently visible.
bar_states: dict[int, bool] = {}


def toggle_bar(qtile) -> None:
    """Toggle the visibility of bars on all screens.

    The function respects the initial value stored in ``bar_states`` or falls
    back to ``DEFAULT_BAR_VISIBILITY`` when a screen is toggled for the first
    time.
    """

    for i, screen in enumerate(qtile.screens):
        bar = screen.bottom
        visible = bar_states.get(i, DEFAULT_BAR_VISIBILITY)

        # Show the bar if it is currently hidden and vice versa.
        bar.show(not visible)

        # Store the updated visibility state.
        bar_states[i] = not visible
