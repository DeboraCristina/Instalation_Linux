import InstalacaoBasica as basica
import InstalacaoCompleta as completa
import InstalarProgramas as programas
import Utils as u


def main():
    if u.is_sudo():
        u.print_falha("É necessário executar esse programa \nsem privilégios de super usuário!")
        print('\n\n\n')
        input('\t\t[pressione qualquer tecla para continuar...]')
        return


    menu = """
+------------------------------------------------+
|                INSTALAÇÃO LINUX                |
+------------------------------------------------+
| [ 1 ] Instalação Básica                        |
| [ 2 ] Instalação Completa                      |
| [ 3 ] Baixar Programas                         |
|             (Somente após instalação Completa) |
| [ 4 ] Sair                                     |
+------------------------------------------------+
"""

    while True:
        u.executar_comando('clear')

        print(menu)

        try:
            op = int(input(": "))

            if op < 1 or op > 4:
                u.print_falha("Opção inválida")
                print('\n\n\n')
                input('\t\t[pressione qualquer tecla para continuar...]')
            else:
                if op == 1:
                    u.print_sucesso("Escolheu Instalação Básica")
                    print('\n\n\n')
                    input('\t\t[pressione qualquer tecla para continuar...]')
                    basica.instalacao_basica()
                if op == 2:
                    u.print_sucesso("Escolheu Instalação Completa")
                    print('\n\n\n')
                    input('\t\t[pressione qualquer tecla para continuar...]')
                    completa.instalacao_completa()
                if op == 3:
                    programas.instalar_programas()
                    print('Pode acessar essa funcionalidade mais vezes')
                    print('\n\n\n')
                    input('\t\t[pressione qualquer tecla para continuar...]')
                if op == 4:
                    u.print_sucesso("Sistema encerrado")
                    print('\n\n\n')
                    input('\t\t[pressione qualquer tecla para continuar...]')
                    break
        except KeyboardInterrupt:
            u.print_falha("\nSistema encerrado")
            print('\n\n\n')
            input('\t\t[pressione qualquer tecla para continuar...]')
            break
        except:
            u.print_falha("Opção inválida")
            print('\n\n\n')
            input('\t\t[pressione qualquer tecla para continuar...]')


if __name__ == "__main__":
    main()
