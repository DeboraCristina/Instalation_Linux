import Utils as u


def main():
    while True:
        print('Confirma que foi realizada a instalação manual?')
        op = input('Confirma [sim ou nao]: ').lower()
        if op == 'sim':
            u.executar_comando('echo -n "MANUAL" > $HOME/.tipo_instalacao.txt')
            u.print_sucesso('Instalação de programas habilitada')
            input('...')
        if op == 'sim' or op == 'nao':
            break
        else:
            u.print_falha('Ação inváçida!')

if __name__ == '__main__':
    main()