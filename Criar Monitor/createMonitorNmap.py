# -*- coding: utf-8 -*-

#Abre e lê um arquivo txt com nome "ip_list_nmap.txt" que contem o resultado de um comando "nmap"(que pode varrer faixas de IPs) escrito em um txt
arquivo = open ("ip_list.txt")
list = arquivo.read()
arquivo.close()

#Quebra o arquivo lido antes dos IPs rastreados
list = list.split("\nNmap scan report for ")

#Cria uma lista vazia para adicionar os IPs
ipList = []

#Faz um loop para adicionar os IPs na lista
for i in list:
	ipList.append(i.split("\n")[0])

#Faz um loop começando na posição 2 pois os 2 primeiros elementos gerados não nos interessam. Após isso vai gerar os comandos que devem ser executados para criar os monitores a partir de linha de comando usando o "curl". Basta copiar o resultado gerado e colar para gerar os monitores no ZM
for i in range(2, len(ipList)):
	print "\ncurl -XPOST http://localhost/zm/api/monitors.json -d \"Monitor[Name]=Monitor-"+str(i+1)+"\\"
	print "&Monitor[Function]=Record\\"
	print "&Monitor[Enabled]=1\\"
	print "&Monitor[Type]=Ffmpeg\\"
	print "&Monitor[Path]=rtsp://admin:abcd1234@"+ipList[i]+":554/\\"
	print "&Monitor[Width]=1280\\"
	print "&Monitor[Height]=720\\"
	print "&Monitor[Colours]=3\\"
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
