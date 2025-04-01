from libqtile import qtile

bar_states = {}

def toggle_bar(qtile):
    for i, screen in enumerate(qtile.screens):
        bar = screen.bottom
        if i not in bar_states:
            bar_states[i] = True  # Por defecto la barra está visible

        if bar_states[i]:
            bar.show(False)
        else:
            bar.show(True)

        bar_states[i] = not bar_states[i]
