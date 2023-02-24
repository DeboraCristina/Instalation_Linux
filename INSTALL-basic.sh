# ********************************************* #
# DEFINIÇÕES
local_dos_arquivos="$HOME/install_files"
source "$local_dos_arquivos/variaveis_gerais.sh"
source "$local_dos_arquivos/cores.sh"


# IMPORTAÇÕES
source "$local_dos_arquivos/instalar_programas.sh"
source "$local_dos_arquivos/configurar_vim.sh"
source "$local_dos_arquivos/configurar_zsh.sh"


# INSTALANDO
cd $HOME

instalar_programas_basicos

git clone "https://github.com/DeboraCristina/My-Linux.git"
configurar_zsh
configurar_vim

######
