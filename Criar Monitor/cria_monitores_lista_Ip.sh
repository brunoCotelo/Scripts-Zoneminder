#Roda o script python para criar os monitores
python createMonitorListaIP.py > comandos_curl_lista.sh

#Roda o script bash para rodar os comandos curl
sudo bash comandos_curl_lista.sh
