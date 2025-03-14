# 🎨 Dotfiles de Qtile en Arch Linux

Este repositorio contiene mi configuración personalizada de Qtile en Arch Linux, enfocada en minimalismo, eficiencia y estética. Si estás buscando una configuración ligera, con una interfaz atractiva y completamente personalizable, ¡este es el repo!

---

## 🚀 Tecnologías utilizadas

| Componente | Descripción |
|------------|-------------|
| **Qtile** | Administrador de ventanas en mosaico, completamente programable en Python. |
| **X11** | Servidor de pantalla utilizado. |
| **Ly** | Gestor de sesiones ligero, rápido y visualmente atractivo. |
| **Picom** | Compositor para efectos de transparencia y suavizado de bordes. |
| **Neovim (nvim)** | Editor de texto poderoso y personalizable. |
| **i3lock** | Bloqueo de pantalla minimalista. |
| **Kitty** | Emulador de terminal rápido y con soporte para GPU. |
| **Dunst** | Notificador ligero y configurable. |

---

## 🖥️ Vista previa



---

## 📂 Estructura del repositorio

Este repositorio está organizado de manera modular para facilitar la personalización:

- 📜 `config.py` → Configuración principal de Qtile, importando todos los módulos.
- 🏗️ `layouts.py` → Diseños de ventana personalizados, incluyendo `MonadTall`, `Floating` y `Columns`.
- 🏢 `groups.py` → Espacios de trabajo, etiquetados con iconos NerdFont.
- 📊 `widgets.py` → Configuración de la barra de estado con reloj, WiFi, volumen, y más.
- 🎨 `theme.py` → Esquema de colores y fuentes basado en el tema **Gruvbox**.
- 🔄 `autostart.py` → Scripts de inicio automático.
- 🎹 `keys.py` → Atajos de teclado intuitivos y eficientes.
- 🖱️ `mouse.py` → Configuración de gestos con el mouse.
- 🔔 `hooks.py` → Eventos y comportamientos automáticos (ej. transparencia de ventanas).
- 🏞️ `screens.py` → Configuración de pantallas y barras de estado.
- 🪟 `floating.py` → Configuración de ventanas flotantes.

---

## 🔧 Instalación y configuración

Para instalar esta configuración en tu sistema, sigue estos pasos:

### 📥 Clonar el repositorio
```sh
git clone https://github.com/wonkoly/.dotfiles.git
```

### 🔗 Crear enlaces simbólicos
```sh
ln -sf ~/.dotfiles/.config/qtile/* ~/.config/ # Para crear un enlace simbolico 
# o tambien puedes moverlo
mv ~/.dotfiles/.config/qtile/* ~/.config/
# Da permisos de ejecucion al autostart.sh
chmod +x ~/.dotfiles/.config/qtile/autostart.sh 
```

### 🔄 Reiniciar Qtile
```sh
qtile cmd-obj -o cmd -f restart
```

---

## 📦 Dependencias

Para que esta configuración funcione correctamente en Arch Linux, instala los siguientes paquetes:
```sh
sudo pacman -S qtile ly picom kitty dunst i3lock rofi nerd-fonts-jetbrains-mono
```
Si usas `yay` para paquetes AUR, también puedes instalar `ttf-nerd-fonts-symbols` para mejor compatibilidad de iconos:
```sh
yay -S ttf-nerd-fonts-symbols
```

---

## 🎨 Personalización avanzada

### 🔵 Cambiar colores y fuentes
Modifica `theme.py` para personalizar el esquema de colores y fuentes.

### ⌨️ Editar atajos de teclado
Los atajos de teclado están definidos en `keys.py`. Puedes cambiarlos según tus preferencias.

### 📊 Modificar la barra de estado
Personaliza `widgets.py` para agregar o quitar widgets según tus necesidades.

---

## 🤝 Contribuir

Si deseas aportar mejoras, puedes hacer un **fork** de este repositorio y enviar un **pull request**. ¡Toda colaboración es bienvenida :)!

---

*Este README proporciona una guía detallada sobre la configuración de Qtile en este repositorio. Asegúrate de ajustar las rutas según tu configuración.*

