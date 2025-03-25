import os
import sys

# Ignoramos la configuracion por default
config.load_autoconfig(False)

# Aseguramos que qutebrowser pueda importar desde el mismo direcctiorio
config_dir = os.path.expanduser("~/.config/qutebrowser")
sys.path.insert(0, config_dir)

import theme
import bar
import tabs
import search

theme.apply(c, config)
bar.apply(c, config)
tabs.apply(c, config)
search.apply(c, config)

# Otros detalles
c.editor.command = ["nvim", "{}"]

