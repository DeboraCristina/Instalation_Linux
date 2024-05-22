from PacotesParaInstalacao import *
import Utils as u


def escolher_programas(categoria: Categoria):
    pacotes = categoria.pacotes

    while True:
        u.executar_comando('clear')

        categoria.show()
        p_selecionados = categoria.pacotes_selecionados

        print('Escolha os apps desejados')
        print('*1,2,4*, *1-3*, *4* (Digitar o msm num deseleciona)')
        print('[i] Instala Selecionados; [l] Limpa Seleção; [v] Volta')
        op = input(': ')

        if op.isdigit():
            op = int(op)-1
            try:
                p = pacotes[op]
                if p in p_selecionados:
                    categoria.deselecionar_pacote(p.nome)
                else:
                    categoria.selecionar_pacote(p.nome)
            except Exception as e:
                pass
        elif op.replace(' ', '').replace('-', '').replace(',', '').isnumeric():
            if op.count('-') == 1:
                index = op.split('-')
                inicio = int(index[0]) - 1
                fim = int(index[1])
                for i in range(inicio, fim):
                    try:
                        p = pacotes[i]
                        if p in p_selecionados:
                            categoria.deselecionar_pacote(p.nome)
                        else:
                            categoria.selecionar_pacote(p.nome)
                    except:
                        pass
            if ',' in op:
                index = op.split(',')
                for i in index:
                    i = int(i)-1
                    try:
                        p = pacotes[i]
                        if p in p_selecionados:
                            categoria.deselecionar_pacote(p.nome)
                        else:
                            categoria.selecionar_pacote(p.nome)
                    except:
                        pass
        elif op.lower() == 'i':
            conf = input('Tem certeza? [sim/não] ')
            if conf == 'sim':
                categoria.instalar_selecionados()
        elif op.lower() == 'l':
            categoria.limpar_selecao()
        elif op.lower() == 'v':
            break
        else:
            u.print_falha('Opção invalida')
            input('\t\t[pressione qualquer tecla para continuar...]')


def instalar_programas():
    if u.get_tipo_instalacao() != 'COMPLETA' and u.get_tipo_instalacao() != 'MANUAL':
        raise Exception('É necessário ter feito a instalação completa ou manual \npara baixar os aplicativos')
    
    categorias = [
        terminal,             # 0 - 1
        web,                  # 1 - 2
        notas_organizacao,    # 2 - 3
        desenvolvimento,      # 3 - 4
        ferramentas,          # 4 - 5
    ]

    desenvolvimento.selecionar_pacote('pycharm')

    menu = '===== Escolha uma categoria =====\n'
    cont = 1
    for categoria in categorias:
        menu += f'\t[ {cont} ] {categoria.nome}\n'
        cont += 1
    menu += f'\t[ {cont} ]  - Listar Selecionados\n'
    cont += 1
    menu += f'\t[ {cont} ]  - Instalar Todos\n'
    cont += 1
    menu += f'\t[ {cont} ]  - Cancelar\n'

    while True:
        u.executar_comando('clear')
        print(menu)

        try:
            op = int(input(': '))

            if op < 1 or op > cont:
                raise Exception()
            
            if op == 8:
                break
            if op == 7:
                conf = input('Tem certeza? [sim/não] ')
                if conf == 'sim':
                    for cat in categorias:
                        cat.instalar_selecionados()
            elif op == 6:
                for cat in categorias:
                    cat.show_selecionados()
                input('\t\t[...]')
            elif op >= 1 and op <= 5:
                escolher_programas(categorias[op-1])

        except KeyboardInterrupt:
            u.print_falha("\nFuncuonalidade encerrada de forma inesperada... :(")
            break
        except:
            u.print_falha("Opção inválida")
            print('\n\n\n')
            input('\t\t[pressione qualquer tecla para continuar...]')
    
    return

if __name__ == '__main__':
    instalar_programas()
