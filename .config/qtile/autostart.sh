#!/bin/bash

# Iniciar compositor de transparencia y efectos visuales
picom --config ~/.config/picom/picom.conf &

# Establecer fondo de pantalla con feh
feh --bg-scale ~/Images/soul-eater1.jpg &

# Iniciar el applet de NetworkManager para gestionar redes
nm-applet &
blueman-applet &
volumeicon &
dunst &
cbatticon &

# Configurar teclado (cambia a tu distribución si es necesario)
# setxkbmap us &

# Ajustar la velocidad del cursor del mouse
xset r rate 300 50 &

# Ajustar el brillo de la pantalla al iniciar (opcional, ajusta el valor si es necesario)
brightnessctl set 50% &
