import PacotesParaInstalacao as p
import Utils as u
import Git_GitHub as g
import ConfigurarTerminal as c

HOME = u.get_home()


def instalacao_completa():
    u.executar_comando('echo -n "COMPLETA" > $HOME/.tipo_instalacao.txt')

    u.apt_update()

    u.diretorio_existe(f'{HOME}/Downloads')
    u.diretorio_existe(f'{HOME}/Downloads/GitClone')
    u.diretorio_existe(f'{HOME}/Downloads/InstallLogs')

    p.pacotes_base.instalar_todos()

    # Configurar Flathub caso não tenha
    u.executar_comando('flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')

    # Python
    p.desenvolvimento.instalar_pacote('python tkinter')
    u.executar_comando('pip install PySimpleGUI')

    g.configurar_git_github()

    c.configura_teminal()

    u.apt_update()
    u.executar_comando('sudo apt full-upgrade')

    return