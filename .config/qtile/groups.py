from libqtile.config import Group

# Diccionario de iconos por grupo
group_icons = {
    "1": " ",  # Terminal
    "2": " ",  # Navegador
    "3": "󰨞 ",  # Código / Edición
    "4": " ",  # Aplicaciones varias
    "5": " ",  # Spotify
}

# Crear los grupos con nombre numérico y etiqueta de icono
groups = [Group(name, label=icon) for name, icon in group_icons.items()]
