from Pacote import Pacote

class Categoria:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.pacotes = list()
        self.pacotes_selecionados = list()
        return
    
    def selecionar_pacote(self, nome_pacote: str) -> bool:
        pacote = self.get_pacote(nome_pacote)
        if pacote in self.pacotes:
            self.pacotes_selecionados.append(pacote)
            return True
        return False
    
    def deselecionar_pacote(self, nome_pacote: str) -> bool:
        pacote = self.get_pacote(nome_pacote)
        if pacote in self.pacotes:
            self.pacotes_selecionados.remove(pacote)
            return True
        return False
    
    def limpar_selecao(self) -> None:
        self.pacotes_selecionados.clear()
        return
    
    def add_pacote(self, pacote: Pacote) -> None:
        self.pacotes.append(pacote)
        return

    def show_selecionados(self) -> None:
        if len(self.pacotes_selecionados) > 0:
            print(f'Mostrando pacotes selecionados da Categoria: {self.nome}')
            for pacote in self.pacotes_selecionados:
                print(f'\t-> {pacote.nome}')
            print('')
        return

    def show(self) -> None:
        print(f'Mostrando pacotes da Categoria: {self.nome}')
        i = 1
        for pacote in self.pacotes:
            msg = '\t'
            if pacote in self.pacotes_selecionados:
                msg += '* '
            msg += f'[ {i} ] {pacote.nome}'
            i += 1
            print(msg)
        print('')
        return
    
    def get_nomes_pacotes(self) -> list:
        nomes_pacotes = []
        for pacote in self.pacotes:
            nomes_pacotes.append(pacote.nome)
        return nomes_pacotes
    
    def get_pacote(self, nome_pacote: str) -> Pacote:
        pacote = None
        for p in self.pacotes:
            if p.nome == nome_pacote:
                pacote = p
                break
        return pacote

    def instalar_todos(self) -> None:
        for pacote in self.pacotes:
            pacote.instalar()
        return

    def instalar_selecionados(self) -> None:
        for pacote in self.pacotes_selecionados:
            pacote.instalar()
        return

    def instalar_pacote(self, nome_pacote: str) -> None:
        pacote = None
        for p in self.pacotes:
            if p.nome == nome_pacote:
                pacote = p
                break
        pacote.instalar()
        return
