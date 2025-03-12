from libqtile import layout

layouts = [
    layout.MonadTall(margin=10, border_width=2, border_focus="#d79921", border_normal="#282828"),
    layout.MonadWide(margin=10, border_width=2, border_focus="#d79921", border_normal="#282828"),
    layout.Floating(border_width=2, border_focus="#d79921", border_normal="#282828"),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
]