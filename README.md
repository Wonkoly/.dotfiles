# Dotfiles para Qtile y Arch Linux

Este repositorio contiene la configuración personalizada de Qtile y otros dotfiles para mi entorno en Arch Linux.

## 📂 Estructura del Repositorio
```
~/.dotfiles
├── .config
│   ├── qtile
│   │   ├── autostart.py       # Script de inicio automático
│   │   ├── autostart.sh       # Ejecuta procesos en segundo plano
│   │   ├── config.py          # Configuración principal de Qtile
│   │   ├── floating.py        # Configuración de ventanas flotantes
│   │   ├── groups.py          # Configuración de los grupos de trabajo
│   │   ├── hooks.py           # Hooks para eventos específicos
│   │   ├── keys.py            # Atajos de teclado personalizados
│   │   ├── layouts.py         # Configuración de los layouts
│   │   ├── mouse.py           # Configuración del ratón
│   │   ├── screens.py         # Configuración de las pantallas y la barra
│   │   ├── theme.py           # Configuración de colores y temas
│   │   ├── widgets.py         # Configuración de los widgets
│   ├── otras_carpetas...      # Otros dotfiles
├── .gitignore                 # Archivos a ignorar en el repositorio
├── README.md                  # Este archivo
```

## 🛠️ Instalación

### 1️⃣ Clonar el repositorio

```sh
git clone --bare https://github.com/tu-usuario/dotfiles.git $HOME/.dotfiles
```

### 2️⃣ Definir alias para gestionar los dotfiles

```sh
alias dotfiles='git --git-dir=$HOME/.dotfiles --work-tree=$HOME'
```

### 3️⃣ Aplicar los dotfiles en el sistema

```sh
dotfiles checkout
```
Si hay conflictos, puedes resolverlos moviendo archivos en conflicto:
```sh
mkdir -p ~/.dotfiles-backup
rsync -av --progress ~/.config/qtile ~/.dotfiles-backup/
dotfiles checkout
```

### 4️⃣ Ignorar archivos no deseados

```sh
dotfiles config --local status.showUntrackedFiles no
```

### 5️⃣ Instalar dependencias necesarias
```sh
sudo pacman -S qtile rofi alacritty brightnessctl pulseaudio pavucontrol
```

## 🚀 Uso

Para actualizar y sincronizar cambios:
```sh
dotfiles status
dotfiles add .config/qtile/config.py
dotfiles commit -m "Actualización de configuración"
dotfiles push
```

Si quieres eliminar un enlace simbólico:
```sh
rm ~/.config/qtile
```

---

Este repositorio permite una fácil administración y versionado de mis configuraciones personales en Arch Linux con Qtile.


