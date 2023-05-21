# -*- coding: utf-8 -*-

#Vale ressaltar que para que esse scipt funcione corretamente deve-se ter um arquivo CSV nomeado de ip_list.csv que contenha 3 colunas: o andar, a localização e o IP das cameras


#Importa a biblioteca para ler o arquivo CSV
import csv

# Abrir o arquivo CSV
with open('ip_list.csv') as arquivo_csv:

	# Criar um objeto reader CSV
	leitor_csv = csv.reader(arquivo_csv, delimiter=',')
	#Cria uma lista vazia para armazenar as linhas
	lista = []
    	# Para cada linha no arquivo
    	for linha in leitor_csv:
		#Adiciona a linha na lista
		lista.append(linha)        

#Faz um loop percorrendo a lista gerada para gerar os comandos que devem ser executados para criar os monitores a partir de linha de comando usando o "curl". Basta copiar o resultado gerado e colar para gerar os monitores no ZM
	for linha in lista:  	
		print "\ncurl -XPOST http://localhost/zm/api/monitors.json -d \"Monitor[Name]={} - {}\\".format(linha[0], linha[1])
		print "&Monitor[Function]=Record\\"
		print "&Monitor[Enabled]=1\\"
		print "&Monitor[Type]=Ffmpeg\\"
		print "&Monitor[Path]=rtsp://admin:abcd1234@{}:554/\\".format(linha[2])
		print "&Monitor[Width]=1280\\"
		print "&Monitor[Height]=720\\"
		print "&Monitor[Colours]=4\\"
		print "&Monitor[ImageBufferCount]=20\\"
		print "&Monitor[WarmupCount]=0\\"
		print "Monitor[PreEventCount]=5\\"
		print "&Monitor[PostEventCount]=5\\"
		print "&Monitor[StreamReplayBuffer]=0\\"
		print "&Monitor[FPSReportInterval]=100\\"
		print "&Monitor[SaveJPEGs]=0\\"
		print "&Monitor[VideoWriter]=2\\"
		print "&Monitor[WebColour]=#4e9a06\\"
		print "&Monitor[AlarmFrameCount]=1\""
		print "\n"
