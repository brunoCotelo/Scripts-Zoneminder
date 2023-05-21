# -*- coding: utf-8 -*-

#Abre e lê um arquivo txt com nome "ip_list2.txt" que contem uma lista de IPs com quebra de linha a cada IP
arquivo = open ("ip_list2.txt")
list = arquivo.read()
arquivo.close()

#Quebra a lista a cada quebra de linha em elementos, resultando em um IP por elemento
list = list.split("\n")

#Faz um loop percorrendo a lista gerada para gerar os comandos que devem ser executados para criar os monitores a partir de linha de comando usando o "curl". Basta copiar o resultado gerado e colar para gerar os monitores no ZM
for i in range(len(list)):
  	print "\ncurl -XPOST http://localhost/zm/api/monitors.json -d \"Monitor[Name]=Monitor-"+str(i+1)+"\\"
	print "&Monitor[Function]=Record\\"
	print "&Monitor[Enabled]=1\\"
	print "&Monitor[Type]=Ffmpeg\\"
	print "&Monitor[Path]=rtsp://admin:abcd1234@"+list[i]+":554/\\"
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
