from libqtile import hook

# Transparencias
@hook.subscribe.client_managed
def set_transparency(window):
    """Ajusta la transparencia de ventanas específicas."""
    if window.name and "kitty" in window.name:
        window.opacity = 1.3  
    elif window.name and "Firefox" in window.name:
        window.opacity = 1.3  # Firefox
    elif window.name and "Code-OSS" in window.name:
        window.opacity = 1.3 
        
# Asignacion de grupos por aplicaciones
@hook.subscribe.client_managed
def move_window_to_group(window):
    """Mueve ciertas aplicaciones a grupos específicos al abrirse."""
    app_group_map = {
        "firefox": "2",  # Firefox en el grupo 'web'
        "kitty": "1",    # Kitty en el grupo 'term'
        "obsidian": "4",  # Discord en el grupo 'chat'
        "spotify": "5", # Spotify en el grupo 'music'
        "code": "3", # Spotify en el grupo 'music'
    }

    wm_class = window.get_wm_class()  # Obtiene la clase de la ventana
    if wm_class:
        for app, group in app_group_map.items():
            if app in wm_class:
                window.togroup(group)
                break
