import os


class Pacote:
    def __init__(self, instalador: str, pacote: str, nome: str) -> None:
        self.instalador = instalador
        self.pacote = pacote
        self.nome = nome

        if self.instalador != 'apt' and self.instalador != 'flatpak' and self.instalador != 'dowload' \
            and self.instalador != 'deb' and self.instalador != 'git':
            raise Exception("Instalador não reconhecido!\nInstadores reconhecidos: 'apt', 'flatpak', 'dowload', 'deb', 'git'")

        return

    def instalar(self) -> int:
        instalador = self.instalador
        retorno = -1
        if instalador == 'git':
            print(f'\033[1;92m\t\t\t*************** Clonando {self.nome} ***************\033[0m')
            retorno = self.__git_clone()
            print('')
        if instalador == 'deb':
            print(f'\033[1;92m\t\t\t*************** Instalando {self.nome} ***************\033[0m')
            retorno = self.__install_deb()
            print('')
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

    def __install_deb(self) -> int:
        self.__download()
        deb = self.pacote.split('/')[-1]
        cmd = f'sudo apt install -y "$HOME/Downloads/{deb}"'
        return self.__executar_comando(cmd)
    
    def __git_clone(self) -> int:
        cmd = f'git clone {self.pacote} $HOME/Downloads/GitClone/{self.nome}'
        return self.__executar_comando(cmd)
    
    def __install_apt(self) -> int:
        cmd = f'sudo apt install -y {self.pacote}'
        return self.__executar_comando(cmd)

    def __install_flatpack(self) -> int:
        cmd = f'sudo flatpak install -y {self.pacote}'
        return self.__executar_comando(cmd)

    def __download(self) -> int:
        cmd = f'curl -o "$HOME/Downloads/{self.nome}" {self.pacote}'
        return self.__executar_comando(cmd)

    def __executar_comando(self, comando: str) -> int:
        resultado = os.system(comando)
        return resultado
