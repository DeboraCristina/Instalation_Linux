import os


def executar_comando(comando: str) -> int:
    resultado = os.system(comando)
    return resultado


def is_sudo() -> bool:
    id = os.geteuid()
    if id == 0:
        return True
    return False


def apt_update():
    executar_comando('sudo apt update')
    return


def diretorio_existe(diretorio):
    if not os.path.isdir(diretorio):
        print(f'\033[1;93mDiretório {diretorio} não existe. {diretorio} foi criado')
        executar_comando(f'mkdir {diretorio}')
    return


def get_home() -> str:
    return os.path.expanduser("~")


def print_sucesso(msg):
    print(f'\033[1;92m{msg}\033[0m')
    return


def print_falha(msg):
    print(f'\033[1;91m{msg}\033[0m')
    return


def get_tipo_instalacao():
    with open(f'{get_home()}/.tipo_instalacao.txt', 'r') as fd:
        tipo = fd.read()
    return tipo
