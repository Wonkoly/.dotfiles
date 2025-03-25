def apply(c, config):
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
