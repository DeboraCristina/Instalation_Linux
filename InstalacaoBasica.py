import PacotesParaInstalacao as p
import Utils as u

HOME = u.get_home()


def instalacao_basica():
    u.executar_comando('echo -n "BÁSICA" > $HOME/.tipo_instalacao.txt')

    u.apt_update()

    u.diretorio_existe(f'{HOME}/Downloads/InstallLogs')

    p.pacotes_base.instalar_pacote('git')
    p.pacotes_base.instalar_pacote('vim')
    p.pacotes_base.instalar_pacote('zsh')

    u.apt_update()
    u.executar_comando('sudo apt full-upgrade')
    return
