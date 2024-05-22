from Pacote import Pacote

class Categoria:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.pacotes = list()
        return
    
    def add_pacote(self, pacote: Pacote) -> None:
        self.pacotes.append(pacote)
        return

    def show(self) -> None:
        print(f'Mostrando pacotes da Categoria: {self.nome}')
        for pacote in self.pacotes:
            print(f'\t-> {pacote.nome}')
        print('')

    def instalar_todos(self) -> int:
        for pacote in self.pacotes:
            pacote.instalar()

    def instalar_pacote(self, nome_pacote: str) -> int:
        pacote = None
        for p in self.pacotes:
            if p.nome == nome_pacote:
                pacote = p
                break
        pacote.instalar()
