import os


class Pacote:
    def __init__(self, instalador: str, pacote: str, nome: str) -> None:
        self.instalador = instalador
        self.pacote = pacote
        self.nome = nome

        if self.instalador != 'apt' and self.instalador != 'flatpak' and self.instalador != 'dowload':
            raise Exception("Instalador não reconhecido!\nInstadores reconhecidos: 'apt', 'flatpak', 'dowload'")

        return

    def instalar(self) -> int:
        instalador = self.instalador
        retorno = -1
        if instalador == 'apt':
            print(f'\033[1;92m\t\t\t*************** Instalando {self.nome} ***************\033[0m')
            retorno = self.__install_apt()
            print('')
        if instalador == 'flatpak':
            print(f'\033[1;92m\t\t\t*************** Instalando {self.nome} ***************\033[0m')
            retorno = self.__install_flatpack()
            print('')
        if instalador == 'dowload':
            print(f'\033[1;92m\t\t\t*************** Baixando {self.nome} ***************\033[0m')
            retorno = self.__download()
            print('')
        return retorno

    def __install_apt(self) -> int:
        cmd = f'sudo apt install -y {self.pacote}'
        return self.executar_comando(cmd)

    def __install_flatpack(self) -> int:
        cmd = f'sudo flatpak install -y {self.pacote}'
        return self.executar_comando(cmd)

    def __download(self) -> int:
        cmd = f'curl -o "$HOME/Downloads/{self.nome}" {self.pacote}'
        return self.executar_comando(cmd)

    def executar_comando(self, comando: str) -> int:
        resultado = os.system(comando)
        return resultado
