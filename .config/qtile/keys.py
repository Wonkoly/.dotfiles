from libqtile.config import Key
from libqtile.lazy import lazy
from groups import groups

mod = "mod4"
terminal = "kitty"
browser = "firefox"
explor_file = "pcmanfm"

keys = [

    # Movimiento Foco
    Key([mod], "h", lazy.layout.left(), desc="Mover foco a la izquierda"),
    Key([mod], "l", lazy.layout.right(), desc="Mover foco a la derecha"),
    Key([mod], "j", lazy.layout.down(), desc="Mover foco abajo"),
    Key([mod], "k", lazy.layout.up(), desc="Mover foco arriba"),
    Key([mod], "Tab", lazy.layout.next(), desc="Mover foco a otra ventana"),
    
    # Movimiento Ventana
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Mover ventana a la izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Mover ventana a la derecha"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Mover ventana abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Mover ventana arriba"),

    # Atajos Teclado
    Key([mod], "Return", lazy.spawn(terminal), desc="Abrir terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Cerrar ventana"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Recargar configuración"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Cerrar sesión"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Abrir Rofi"),
    Key([mod], "f", lazy.spawn(browser), desc="Abre el navegador por defecto"),
    Key([mod], "e", lazy.spawn(explor_file), desc="Abre el navegador de archivos por defecto"),

    # Atajo Cambio de Teclados
    Key([mod], "z", lazy.spawn("setxkbmap -layout us,latam -option grp:alt_shift_toggle"), desc="Alternar entre inglés y español"),

    # Volumen
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Subir volumen"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Bajar volumen"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Silenciar volumen"),
    
    # Brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Subir brillo"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Bajar brillo"),

]

# Atajos para cambiar de grupo y mover ventanas
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Ir al grupo {i.name}"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Mover ventana al grupo {i.name}"),
    ])
