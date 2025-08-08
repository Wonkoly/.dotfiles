from libqtile.config import Match
from libqtile import layout
from theme import colors

floating_layout = layout.Floating(
    border_width=2,
    border_focus=colors["border"],
    border_normal=colors["background"],
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)
