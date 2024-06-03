from Categoria import Categoria
from Pacote import Pacote


### TEMPLATE
## NOVA CATEGORIA
# nomeCategoria = Categoria('nomeCategoria')
## ADD PACOTE
# nomeCategoria.add_pacote(Pacote(instalador: str, pacote: str, nome: str))
# nomeCategoria.add_pacote(Pacote(instalador='placeholder', pacote='placeholder', nome='placeholder'))

terminal = Categoria('TERMINAL')
terminal.add_pacote(Pacote('apt', 'tree', 'tree'))
terminal.add_pacote(Pacote('apt', 'bat', 'bat'))

web = Categoria('WEB')
web.add_pacote(Pacote('deb', 'https://download5.operacdn.com/ftp/pub/opera/desktop/110.0.5130.23/linux/opera-stable_110.0.5130.23_amd64.deb', 'Navegador Opera'))
web.add_pacote(Pacote('deb', 'https://mega.nz/linux/repo/xUbuntu_24.04/amd64/megasync-xUbuntu_24.04_amd64.deb', 'Nuvem Mega'))
web.add_pacote(Pacote('deb', 'https://download.anydesk.com/linux/anydesk_6.3.2-1_amd64.deb', 'Anydesk'))
web.add_pacote(Pacote(instalador='deb', pacote='https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_125.0.2535.67-1_amd64.deb?brand=M102', nome='Navegador Edge'))

notas_organizacao = Categoria('NOTAS/ORGANIZAÇÃO')
notas_organizacao.add_pacote(Pacote('flatpak', 'flathub com.toolstack.Folio', 'Folio'))
notas_organizacao.add_pacote(Pacote('flatpak', 'flathub md.obsidian.Obsidian', 'Obsidian'))
notas_organizacao.add_pacote(Pacote('flatpak', 'flathub org.onlyoffice.desktopeditors', 'Onlyoffice'))
notas_organizacao.add_pacote(Pacote('git', 'git@github.com:DeboraCristina/CronogramaSimpleGUI.git', 'Cronograma'))

desenvolvimento = Categoria('DESENVOLVIMENTO')
desenvolvimento.add_pacote(Pacote('flatpak', 'flathub com.jetbrains.IntelliJ-IDEA-Community', 'intellij'))
desenvolvimento.add_pacote(Pacote('dowload', 'https://eclipse.c3sl.ufpr.br/oomph/epp/2024-03/R/eclipse-inst-jre-linux64.tar.gz', 'eclipse'))
desenvolvimento.add_pacote(Pacote('flatpak', 'flathub com.jetbrains.DataGrip', 'datagrip'))
desenvolvimento.add_pacote(Pacote('deb', 'https://vscode.download.prss.microsoft.com/dbazure/download/stable/dc96b837cf6bb4af9cd736aa3af08cf8279f7685/code_1.89.1-1715060508_amd64.deb', 'vscode'))
desenvolvimento.add_pacote(Pacote('flatpak', 'flathub com.jetbrains.PyCharm-Community', 'pycharm'))
desenvolvimento.add_pacote(Pacote('apt', 'python3-tk', 'python tkinter'))
desenvolvimento.add_pacote(Pacote('deb', 'https://download.virtualbox.org/virtualbox/7.0.18/virtualbox-7.0_7.0.18-162988~Ubuntu~jammy_amd64.deb', 'virtual box'))

ferramentas = Categoria('FERRAMENTAS')
ferramentas.add_pacote(Pacote('flatpak', 'flathub com.github.PintaProject.Pinta', 'pinta'))
ferramentas.add_pacote(Pacote('flatpak', 'flathub com.usebottles.bottles', 'bottles'))
ferramentas.add_pacote(Pacote('dowload', 'https://medibangpaint.com/static/installer/MediBangPaintPro/MediBangPaintProSetup-29.1-64bit.exe', 'medibang paint'))
ferramentas.add_pacote(Pacote('apt', 'mousepad', 'mousepad'))
ferramentas.add_pacote(Pacote('apt', 'tilix', 'tilix'))
ferramentas.add_pacote(Pacote('apt', 'flameshot', 'Flameshot'))
ferramentas.add_pacote(Pacote(instalador='deb', pacote='https://download3.ebz.epson.net/dsc/f/03/00/15/64/87/08cd9b6782b8387cb5ddd27486da65fb2548f13a/epson-inkjet-printer-201207w_1.0.1-1_amd64.deb', nome='Driver Impressora L355'))

pacotes_base = Categoria('PACOTES_BASE')
pacotes_base.add_pacote(Pacote('apt', 'git', 'git'))
pacotes_base.add_pacote(Pacote('apt', 'zsh', 'zsh'))
pacotes_base.add_pacote(Pacote('apt', 'manpages', 'manpages'))
pacotes_base.add_pacote(Pacote('apt', 'man-db', 'man-db'))
pacotes_base.add_pacote(Pacote('apt', 'flatpak', 'flatpak'))
pacotes_base.add_pacote(Pacote('apt', 'curl', 'curl'))
pacotes_base.add_pacote(Pacote('apt', 'vim', 'vim'))
pacotes_base.add_pacote(Pacote('apt', 'python3-pip', 'python pip'))