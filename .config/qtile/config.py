from libqtile import hook
import hooks
from keys import keys
from groups import groups
from layouts import layouts
from widgets import widget_defaults, widgets
from screens import screens
from mouse import mouse
from floating import floating_layout
from autostart import autostart

mod = "mod4"

@hook.subscribe.startup_once
def start_once():
    autostart()

# Configuración general
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "Cokie 󰆘"
