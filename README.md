# Configuración Avanzada de Qtile

Este repositorio contiene una configuración altamente personalizada de **Qtile**, diseñada para maximizar la productividad y eficiencia en un entorno de escritorio minimalista y altamente configurable.

## 📌 Características Destacadas
- **Tema:** Uso de la paleta de colores **Gruvbox**.
- **Diseños de Ventana:** MonadTall, MonadWide, Floating, Columns y Max.
- **Widgets Personalizados:** Información sobre batería, red, hora, brillo y más.
- **Atajos de Teclado:** Navegación rápida y fluida.
- **Sistema de Autoinicio:** Para ejecutar aplicaciones esenciales al inicio.
- **Transparencia en Ventanas:** Soporte para Kitty, Firefox y VS Code.
- **Integración con Rofi:** Lanzador de aplicaciones dinámico.
- **Soporte para Multimedia:** Control de brillo y volumen mediante teclas especiales.
- **Compatibilidad con Múltiples Monitores.**

## 📂 Repositorio
El código fuente y configuración completa se encuentran en **[.dotfiles](https://github.com/Wonkoly/.dotfiles)**.

## 🛠️ Requisitos
Asegúrate de tener instalados los siguientes paquetes:
```bash
sudo pacman -S qtile rofi kitty firefox pcmanfm brightnessctl pulseaudio pavucontrol network-manager-applet
```
Para usuarios de Fedora:
```bash
sudo dnf install qtile rofi kitty firefox pcmanfm brightnessctl pulseaudio-utils pavucontrol network-manager-applet
```

## 📥 Instalación
Clona este repositorio en la carpeta de configuración:
```bash
git clone https://github.com/Wonkoly/.dotfiles ~/.config/qtile
```

Otorga permisos de ejecución al script de autoinicio:
```bash
chmod +x ~/.config/qtile/autostart.sh
```

Selecciona **Qtile** como tu gestor de ventanas en tu gestor de sesiones.

## 🏗️ Estructura del Proyecto
- `config.py` - Archivo principal que une todas las configuraciones.
- `keys.py` - Definición de atajos de teclado.
- `groups.py` - Configuración de grupos y etiquetas personalizadas.
- `layouts.py` - Diseño de las ventanas.
- `widgets.py` - Configuración de widgets.
- `screens.py` - Barra de estado y pantallas.
- `autostart.py` - Script de autoinicio.
- `autostart.sh` - Aplicaciones que se ejecutan al iniciar Qtile.
- `mouse.py` - Configuración del ratón.
- `hooks.py` - Hooks personalizados para eventos.
- `floating.py` - Configuración de ventanas flotantes.
- `theme.py` - Paleta de colores y fuentes.

## 🖥️ Uso de Qtile
Algunos de los atajos de teclado más útiles:
- **Cambio de Grupo:** `MOD + [1-5]`
- **Mover Ventanas entre Grupos:** `MOD + Shift + [1-5]`
- **Abrir Terminal:** `MOD + Enter`
- **Abrir Navegador:** `MOD + F`
- **Explorador de Archivos:** `MOD + E`
- **Lanzador de Aplicaciones (Rofi):** `MOD + Space`
- **Recargar Configuración:** `MOD + Control + R`
- **Salir de Qtile:** `MOD + Control + Q`
- **Control de Volumen:** `XF86AudioRaiseVolume / XF86AudioLowerVolume / XF86AudioMute`
- **Ajuste de Brillo:** `XF86MonBrightnessUp / XF86MonBrightnessDown`

## 🎨 Personalización Adicional
Si deseas modificar colores, fuentes o estilos, edita el archivo `theme.py`.
Para modificar widgets, edita `widgets.py`. 

## 🚀 ToDo
- **Soporte para Wayland con Qtile Next.**
- **Mejor gestión de ventanas flotantes.**
- **Integración de cava Widget y otros indicadores.**


## 📜 Licencia
Este proyecto es de código abierto y está bajo la licencia **MIT**.


