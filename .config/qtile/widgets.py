from libqtile import widget
from libqtile import qtile
from theme import colors, font, font_size, bar_size

widget_defaults = dict(
    font="CaskaydiaMono Nerd Font",
    fontsize=14,
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
    widget.Clock(format="%Y-%m-%d %H:%M"),
    widget.Spacer(),
    widget.Battery(
        format="{percent:2.0%}  ",  # Muestra el porcentaje de batería
        update_interval=10,  # Se actualiza cada 10 segundos
        charge_char="⚡",  # Icono cuando está cargando
        discharge_char="🔋",  # Icono cuando está descargando
        empty_char="❌",  # Icono cuando la batería está vacía
        full_char="✅",  #
    ),
    widget.Backlight(
        backlight_name="intel_backlight",  # Cambia esto según tu hardware
        format="󰛨   {percent:2.0%}",  # Muestra el brillo en porcentaje
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
            "Button2": lambda: qtile.cmd_spawn("systemctl suspend"),  # Suspender
            "Button3": lambda: qtile.cmd_spawn("i3lock -c 000000"),  # Bloquear pantalla
        },
        foreground=colors["foreground"],
        padding=10,
    ),
]
