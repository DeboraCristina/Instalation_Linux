instalar()
{
	sudo $gerenciadorPacotes $flag install $1
}

instalar_programas_basicos()
{
	instalar git
	instalar python3-pip
	instalar vim
	instalar zsh
	instalar bat # substitue cat
}

instalar_programas_repositorio()
{
	instalar virtualbox
	instalar megasync
	instalar nemo-megasync
	instalar tldr # substitue a flag --help
}

instalar_programas_flatpak()
{
	# Programação
	flatpak install -y flathub com.jetbrains.PyCharm-Community
	flatpak install -y flathub com.jetbrains.IntelliJ-IDEA-Community
	## flatpak install -y flathub com.jetbrains.GoLand
	## flatpak install -y flathub com.visualstudio.code
	# Produtividade
	flatpak install -y flathub md.obsidian.Obsidian
	flatpak install -y flathub org.flameshot.Flameshot
	## flatpak install -y flathub com.github.PintaProject.Pinta
	# Jogos
	## flatpak install -y flathub net.lutris.Lutris
	flatpak install -y flathub com.valvesoftware.Steam
	# Outros
	flatpak install -y flathub com.dropbox.Client
	## flatpak install -y flathub nz.mega.MEGAsync
	flatpak install -y flathub org.onlyoffice.desktopeditors
	flatpak install -y flathub com.usebottles.bottles
}

instalar_programas_outros()
{
	firefox $MediBangLink
}


instalar_tudo()
{
	instalar_programas_basicos()
	instalar_programas_repositorio()
	instalar_programas_flatpak()
	instalar_programas_outros()

	sudo $gerenciadorPacotes update
}
