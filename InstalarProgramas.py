from PacotesParaInstalacao import *
import Utils as u

HOME = u.get_home()


def escolher_programas(categoria: Categoria):
    pacotes = categoria.pacotes

    while True:
        u.executar_comando('clear')

        categoria.show()
        p_selecionados = categoria.pacotes_selecionados

        print('Escolha os pacotes desejados')
        print('*1,2,4*; *1-3*; *4*')
        print('(Escolher a mesma opção, a deseleciona)')
        print('[i] Instala Selecionados; [l] Limpa Seleção; [v] Volta; [t] Todos')
        op = input(': ')

        # Se for escolhido apenas 1 pacote
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
        
        # Se for escolhido um range de pacotes
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
        elif op.lower() == 't':
            for pacote in pacotes:
                try:
                    categoria.selecionar_pacote(pacote.nome)
                except:
                    pass
        elif op.lower() == 'v':
            break
        else:
            u.print_falha('Opção invalida')
            input('\t\t[pressione qualquer tecla para continuar...]')


def instalar_programas():
    if u.get_tipo_instalacao() != 'COMPLETA' and u.get_tipo_instalacao() != 'MANUAL':
        u.print_falha('É necessário ter feito a instalação completa ou manual \npara baixar os aplicativos')
        input('\t\t[pressione qualquer tecla para continuar...]')
        return
    
    categorias = [
        terminal,             # 0 - 1
        web,                  # 1 - 2
        notas_organizacao,    # 2 - 3
        desenvolvimento,      # 3 - 4
        ferramentas,          # 4 - 5
    ]

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
                input('\t\t[...]')
            elif op == 6:
                for cat in categorias:
                    cat.show_selecionados()
                input('\t\t[...]')
            elif op >= 1 and op <= 5:
                escolher_programas(categorias[op-1])
                input('\t\t[pressione qualquer tecla para continuar...]')

        except KeyboardInterrupt:
            u.print_falha("\nFuncionalidade encerrada de forma inesperada... :(")
            break
        except:
            u.print_falha("Opção inválida")
            print('\n\n\n')
            input('\t\t[pressione qualquer tecla para continuar...]')
    
    return

if __name__ == '__main__':
    u.diretorio_existe(f'{HOME}/Downloads')
    u.diretorio_existe(f'{HOME}/Downloads/GitClone')
    u.diretorio_existe(f'{HOME}/Downloads/InstallLogs')
    u.diretorio_existe(f'{HOME}/Downloads/InstallLinux')
    u.diretorio_existe(f'{HOME}/Downloads/InstallLinux/PacotesWeb')
    instalar_programas()
