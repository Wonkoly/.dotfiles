if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"


# ZSH_THEME="robbyrussell"
ZSH_THEME="powerlevel10k/powerlevel10k"

# Instalacion de Plugins
plugins=(
  git
)

source $ZSH/oh-my-zsh.sh

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='nvim'
fi

command_not_found_handler() {
  if [[ -f "$1" ]]; then
    echo "📂 Abriendo archivo '$1' con Neovim..."
    nvim "$1"
  elif [[ -d "$1" ]]; then
    echo "📁 '$1' es una carpeta. Usa 'cd' para acceder."
  else
    echo "❌ Comando o archivo '$1' no encontrado."
  fi
  return 127
}

#-- ALIASES
alias zshconfig="mate ~/.zshrc"
alias ohmyzsh="mate ~/.oh-my-zsh"
alias logs="bat ~/.local/share/qtile/qtile.log"
alias rmlogs="truncate -s 0 ~/.local/share/qtile/qtile.log && qtile cmd-obj -o cmd -f restart"


#- APPS Aliases
alias py="/sbin/python"
alias cat="/sbin/bat --paging=never"

alias ls="/sbin/lsd"
alias ll="/sbin/lsd -l"
alias la="/sbin/lsd -la"
alias lt="/sbin/lsd --tree"


# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

