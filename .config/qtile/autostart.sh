#!/bin/bash

# Iniciar compositor de transparencia y efectos visuales
picom --config ~/.config/picom/picom.conf &

# Establecer fondo de pantalla con feh
feh --bg-scale ~/Images/soul-eater-grovbox.png &

# Iniciar el applet de NetworkManager para gestionar redes
nm-applet &

# Iniciar el control de volumen en la bandeja del sistema
pa-applet &

# Iniciar el gestor de portapapeles (clipit o copyq)
copyq &

# Iniciar notificaciones
dunst &

# Iniciar el indicador de batería (si usas una laptop)
cbatticon &

# Configurar teclado (cambia a tu distribución si es necesario)
setxkbmap latam &

# Ajustar la velocidad del cursor del mouse
xset r rate 300 50 &

# Ajustar el brillo de la pantalla al iniciar (opcional, ajusta el valor si es necesario)
brightnessctl set 50% &
