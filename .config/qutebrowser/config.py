# Cargar configuración predeterminada
config.load_autoconfig(False)

# Google como buscador por defecto
c.url.searchengines = {
    'DEFAULT': 'https://www.google.com/search?q={}',
    'g': 'https://www.google.com/search?q={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'ddg': 'https://duckduckgo.com/?q={}',
}

# Página de inicio
c.url.start_pages = ['https://www.google.com']
c.url.default_page = 'https://www.google.com'

# Fuente CaskaydiaMono (de NerdFont)
c.fonts.default_family = [
    'CaskaydiaMono Nerd Font',
    'Noto Color Emoji',
    'Noto Sans',
]

c.fonts.default_size = '12pt'

# Tema estilo Gruvbox (oscuro cálido)
# Paleta Gruvbox
bg0 = '#282828'
bg1 = '#3c3836'
bg2 = '#504945'
fg0 = '#fbf1c7'
fg1 = '#ebdbb2'
red = '#cc241d'
green = '#98971a'
yellow = '#d79921'
blue = '#458588'
purple = '#b16286'
aqua = '#689d6a'
orange = '#d65d0e'

# Colores generales
c.colors.completion.fg = fg1
c.colors.completion.odd.bg = bg0
c.colors.completion.even.bg = bg1
c.colors.completion.category.fg = yellow
c.colors.completion.category.bg = bg0
c.colors.completion.item.selected.fg = fg1
c.colors.completion.item.selected.bg = bg2
c.colors.completion.item.selected.border.top = yellow
c.colors.completion.item.selected.border.bottom = yellow

# Barra de estado
c.colors.statusbar.normal.bg = bg0
c.colors.statusbar.insert.bg = green
c.colors.statusbar.command.bg = bg1
c.colors.statusbar.command.fg = fg1
c.colors.statusbar.url.fg = blue
c.colors.statusbar.url.hover.fg = aqua
c.colors.statusbar.url.success.http.fg = green
c.colors.statusbar.url.success.https.fg = green
c.colors.statusbar.url.warn.fg = yellow
c.colors.statusbar.url.error.fg = red

# Barra de estado más grande y visible
c.fonts.statusbar = '10pt CaskaydiaMono Nerd Font'

# Aumentar el padding de la barra de estado
c.statusbar.padding = {
    'top': 7,
    'bottom': 7,
    'left': 9,
    'right': 9,
}

# Pestañas
c.colors.tabs.bar.bg = bg0
c.colors.tabs.odd.bg = bg1
c.colors.tabs.even.bg = bg2
c.colors.tabs.selected.odd.bg = blue
c.colors.tabs.selected.even.bg = blue
c.colors.tabs.selected.odd.fg = fg0
c.colors.tabs.selected.even.fg = fg0

# Mensajes (errores, info, etc.)
c.colors.messages.error.bg = red
c.colors.messages.warning.bg = yellow
c.colors.messages.info.bg = blue

# Interfaz web
c.colors.webpage.bg = bg0
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'smart'

# Otros detalles
c.editor.command = ["nvim", "{}"]

