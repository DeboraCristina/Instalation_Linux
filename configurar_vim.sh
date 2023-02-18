instalar_vundle(){ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim; }
	
configurar_vim()
{
	instalar_vundle
	echo "let \$config = '$arquivo_de_configuracao_vim'
	source \$config" > .vimrc
}
