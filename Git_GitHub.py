from Utils import *


def cliente_ssh_instalado() -> bool:
    with os.popen('apt list | grep ^openssh') as cmd:
        cmd_exit = cmd.read()
    if 'openssh-client' in cmd_exit:
        return True
    return False


def instalar_cliente_ssh():
    executar_comando('sudo apt install -y openssh-client')
    return


def config_git(email, user_name):
    os.system(f'git config --global user.email "{email}"')
    os.system(f'git config --global user.name	"{user_name}"')
    return


def generar_chave(email):
    os.system(f'ssh-keygen -t rsa -b 4096 -C "{email}"')
    os.system('''eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
cat ~/.ssh/id_rsa.pub > $HOME/.SSHKEY''')
    return


def gerar_chave_ssh(email, user_name):
    if not cliente_ssh_instalado():
        instalar_cliente_ssh()
    
    config_git(email, user_name)
    generar_chave(email)
    return


def testar_conexao_github() -> bool:
    result = os.system('git clone git@github.com:DeboraCristina/Libft.git /tmp/testeSSH')
    if result == 0:
        os.system('rm -rf /tmp/testeSSH')
        return True
    return False


def conectar_ao_github():
    falha = 0
    while True:
        input('aguardando conexão com github... [aperte qualquer tecla qnd estivar pronta]')
        conexao = testar_conexao_github()
        if conexao:
            print_sucesso('Conexão feita com Sucesso')
            break
        else:
            if falha < 2:
                print_falha('Não foi possível conectar :( \nSe o erro persistir execute ReconfiguraGit.py')
            else:
                print_falha('Não foi possível conectar :(')
                print_falha('Se o erro persistir abra o arquivo ReconfiguraGit.py e siga o passo a passo!')
            falha += 1
    return


def remover_arquivos_ssh():
    executar_comando('rm -f $HOME/.ssh/*')
    executar_comando('rm -f $HOME/.SSHKEY*')
    return


def configurar_git_github():
    email = 'deboracristinaproficional1@gmail.com'
    user_name = 'DeboraCristina'
    
    gerar_chave_ssh(email, user_name)

    conectar_ao_github()
    return
