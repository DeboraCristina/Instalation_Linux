import Utils as u

def clonar_mylinux(ssh_ativo: bool = True):
    link_ssh = 'git@github.com:DeboraCristina/My-Linux.git'
    link_http = 'https://github.com/DeboraCristina/My-Linux.git'
    destino = '$HOME/My-Linux'
    
    link_padrao = link_ssh
    if not ssh_ativo:
        link_padrao = link_http

    u.executar_comando(f'git clone {link_padrao} {destino}')
    return


def config_vim():
    link_vundle = 'https://github.com/VundleVim/Vundle.vim.git'
    vim_file = '$HOME/My-Linux/Vim-Configs/MyVimConfig'
    u.executar_comando(f'git clone {link_vundle} ~/.vim/bundle/Vundle.vim')
    u.executar_comando(f'echo "let \$config = \'{vim_file}\' \\nsource \$config" > $HOME/.vimrc')
    return


def config_zsh():
    link_oh_my_zsh = 'https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh'
    config_path = '$HOME/My-Linux/zshrc'
    u.executar_comando(f'sh -c "$(curl -fsSL {link_oh_my_zsh})"')
    u.executar_comando(f'mv {config_path} ~/.zshrc')
    return


def configura_teminal(tipo_configuracao:str = 'completa'):
    clonar_mylinux(tipo_configuracao == 'completa')
    
    config_vim()
    config_zsh()
    return


if __name__ == '__main__':
    configura_teminal(tipo_configuracao='BÁSICA')
