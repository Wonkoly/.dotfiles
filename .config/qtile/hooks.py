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