#Escreve os dados dos monitores em um arquivo de texto
curl http://localhost/zm/api/monitors.json > monitors.txt

#Roda o script python para "limpar" o arquivo txt gerado e reescreve ele em outro txt
python id_colect.py > ids.txt

#Roda o script python para gerar os comandos do curl para alterar algum parametro
python change_parameter.py