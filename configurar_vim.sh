instalar_vundle(){ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim; }
	
configurar_vim()
{
	if [ -d "$HOME/My-Linux" ]
	then
		instalar_vundle
		echo "let \$config = '$arquivo_de_configuracao_vim'
		source \$config" > .vimrc
	else
		DEIXAR_TEXTO_VERMELHO
		echo -e "Algo deu errado!\nDiretório com configurações não encontrado\nVIM nao configurado!"
		DEIXAR_TEXTO_NULO
	fi
}
