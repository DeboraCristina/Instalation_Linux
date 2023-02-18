checar_se_a_chave_foi_adicionada()
{
	DEIXAR_TEXTO_BRANCO
	echo -ne "A chave ssh já está configurada no git hub? [s/n]: "
	DEIXAR_TEXTO_CIANO
	read chave_ssh_configurada
	DEIXAR_TEXTO_NULO

	if [ "$chave_ssh_configurada" == "s" ]
	then
		chave_adicionada='true'
	else
		if [ "$chave_ssh_configurada" == "n" ]
		then
			DEIXAR_TEXTO_CIANO
			echo adicione a chave ssh ao git hub para que configurações sejam instaladas completamente
			DEIXAR_TEXTO_NULO
		else
			DEIXAR_TEXTO_VERMELHO
			echo Opcao Invalida!
			DEIXAR_TEXTO_NULO
		fi
	fi
}

checar_chave_github()
{
	while :
	do
		chave_adicionada='false'
		checar_se_a_chave_foi_adicionada
		if [ "$chave_adicionada" == "true" ]
		then
			break
		fi
	done
}
