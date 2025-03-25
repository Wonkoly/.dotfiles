def apply(c, config):
    c.tabs.favicons.show = 'always'  # opciones: 'never', 'pinned', 'always'
    c.tabs.title.format = '{audio}{index}: {current_title}'

# Más espacio en las pestañas (tabs)
    c.tabs.padding = {
        'top': 7,
        'bottom': 7,
        'left': 7,
        'right': 7,
    }