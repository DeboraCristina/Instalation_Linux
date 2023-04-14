# ********************************************* #
# DEFINIÇÕES
local_dos_arquivos="$HOME/install_files"
source "$local_dos_arquivos/variaveis_gerais.sh"
source "$local_dos_arquivos/cores.sh"


# IMPORTAÇÕES
source "$local_dos_arquivos/instalar_programas.sh"
source "$local_dos_arquivos/configurar_python.sh"
source "$local_dos_arquivos/configurar_git.sh"
source "$local_dos_arquivos/gerar_chave_ssh.sh"
source "$local_dos_arquivos/checar_chave_github.sh"
source "$local_dos_arquivos/configurar_vim.sh"
source "$local_dos_arquivos/configurar_zsh.sh"


# INSTALANDO
cd $HOME

instalar_tudo
configurar_git
configurar_python
gerar_chave_ssh
checar_chave_github

if [ "$chave_adicionada" == "true" ]
then
	git clone git@github.com:DeboraCristina/My-Linux.git
	configurar_zsh
	configurar_vim
fi
######
