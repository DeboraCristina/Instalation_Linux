import PacotesParaInstalacao as p
import Utils as u
import ConfigurarTerminal as c

HOME = u.get_home()


def instalacao_basica():
    u.executar_comando('echo -n "BÁSICA" > $HOME/.tipo_instalacao.txt')

    u.apt_update()

    u.diretorio_existe(f'{HOME}/Downloads/InstallLogs')

    p.pacotes_base.instalar_todos()
    
    # Configurar Flathub caso não tenha
    u.executar_comando('flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')
    
    c.configura_teminal(tipo_configuracao='BÁSICA')

    u.apt_update()
    u.executar_comando('sudo apt full-upgrade')
    return
