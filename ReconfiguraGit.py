import Git_GitHub as g


def main():
    g.remover_arquivos_ssh()
    g.generar_chave()
    return


if __name__ == "__main__":
    main()

''' README

# Gerar Chave SSH

> ssh-keygen -t rsa -b 4096 -C "deboracristinaproficional1@gmail.com"

Aperte Enter 3 vezes.
Não ha a necessidade de incluir o file ou a frase.

> eval $(ssh-agent -s) ; ssh-add ~/.ssh/id_rsa

# Pegar a Chave

> cat ~/.ssh/id_rsa.pub >> $HOME/Chave.txt

'''