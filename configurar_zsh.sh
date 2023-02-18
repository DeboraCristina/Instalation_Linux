clonar_ohmyzsh() { sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"; }

configurar_zsh()
{
	if [ -d "$HOME/My-Linux" ]
	then
		clonar_ohmyzsh
		mv $diretorio_de_configuracoes/zshrc "$HOME/.zshrc"

		DEIXAR_TEXTO_VERDE
		echo "ZSH Configurado com Sucesso!"
		DEIXAR_TEXTO_NULO
	else
		DEIXAR_TEXTO_VERMELHO
		echo -e "Algo deu errado!\nDiretório com configurações não encontrado\nZSH nao configurado!"
		DEIXAR_TEXTO_NULO
	fi
}
