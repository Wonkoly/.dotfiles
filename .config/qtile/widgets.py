from libqtile import widget
from libqtile import qtile
from theme import colors, font, font_size

widget_defaults = dict(
    font=font,
    fontsize=font_size,
    padding=5,
)

widgets = [
    widget.GroupBox(
        active=colors["active"],
        inactive=colors["inactive"],
        highlight_method="text",
        this_current_screen_border=colors["highlight"],
        this_screen_border=colors["highlight"],
        other_current_screen_border=colors["inactive"],
        other_screen_border=colors["inactive"],
        fontsize=20,
        padding=3,
    ),
    widget.WindowName(

    ),
    widget.Spacer(),
    widget.Clock(
        format="%Y-%m-%d %H:%M",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("dunstctl history-pop")}
    ),
    widget.Spacer(),
    widget.Backlight(
        backlight_name="intel_backlight",  # Cambia esto según tu hardware
        format="{percent:2.0%}",  # Muestra el brillo en porcentaje
        update_interval=1
    ),
    widget.Wlan(
        interface="wlan0",
        format="{essid}",
        disconnected_message="Sin conexión",
        update_interval=3,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("nm-connection-editor")}
    ),
    widget.Systray(
        icon_size=20,
        padding=5,
    ),
    widget.TextBox(
        text=" ⏻ ",
        fontsize=16,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn("poweroff"),  # Apagar
            "Button3": lambda: qtile.cmd_spawn("lockscreen"),  # Bloquear pantalla
        },
        foreground=colors["foreground"],
        padding=10,
    ),
]
