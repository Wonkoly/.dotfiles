from libqtile import layout
from theme import colors

layouts = [
    layout.MonadTall(
        margin=10,
        border_width=2,
        border_focus=colors["border"],
        border_normal=colors["background"],
    ),
    layout.MonadWide(
        margin=10,
        border_width=2,
        border_focus=colors["border"],
        border_normal=colors["background"],
    ),
    layout.Floating(
        border_width=2,
        border_focus=colors["border"],
        border_normal=colors["background"],
    ),
    layout.Columns(
        border_width=4,
        border_focus=colors["border"],
        border_normal=colors["background"],
        border_focus_stack=[colors["border"], colors["background"]],
    ),
    layout.Max(),
]
