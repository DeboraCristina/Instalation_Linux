configurar_python()
{
	tkinter=""

	if [[ $sys == "arch" ]]
	then
		tkinter="tk"
	fi
	if [[ $sys == "debian" ]]
	then
		tkinter="python-tk"
	else
		echo Sistema Invalido
		exit
	fi
	sudo $gerenciadorPacotes $flag install $tkinter
	pip install PySimpleGUI
}
