gerar_chave_ssh()
{
	ssh-keygen -t rsa -b 4096 -C "$git_mail"
	eval $(ssh-agent -s)
	ssh-add ~/.ssh/id_rsa

	ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

	cat ~/.ssh/id_rsa.pub >>		"$destino_ssh"
}
