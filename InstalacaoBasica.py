import PacotesParaInstalacao as p
import Utils as u


def instalacao_basica():
    u.executar_comando('echo "BÁSICA" > $HOME/.tipo_instalacao.txt')

    u.apt_update()

    p.pacotes_base.instalar_pacote('git')
    p.pacotes_base.instalar_pacote('vim')
    p.pacotes_base.instalar_pacote('zsh')

    u.apt_update()
    u.executar_comando('sudo apt full-upgrade')
    return
