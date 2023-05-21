#Varre a rede e escreve em um arquivo txt
nmap -F 172.20.0-3.0-255 > ip_list.txt

#Move o arquivo da pasta pessoal para a pasta de criar o monitor
mv ip_list.txt /home/monitora/Downloads/Criar_Monitor

#Roda o script python para criar os monitores
python createMonitorNmap.py > comandos_curl.sh

#Roda o script bash para rodar os comandos curl
sudo bash comandos_curl.sh
