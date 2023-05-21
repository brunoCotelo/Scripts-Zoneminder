# -*- coding: utf-8 -*-

#Lê um arquivo com a lista dos IDs de monitores com quebra de linha a cada um gerados pelo id_colect.py e copia para uma lista
arquivo = open ("ids.txt")
lista = arquivo.read()
arquivo.close()

#Quebra a lista em elementos separados por \n, restando em apenas os IDs unicos na lista
lista = lista.split("\n")

#Faz um loop para gerar os comandos curl necessarios para criar as zonas de identificação. Os valores sao altamente variaveis, deve-se checar sempre
for i in range(len(lista)):
	print "\ncurl -XPOST http://localhost/zm/api/zones.json -d \"Zone[Name]=All\\"
	print "&Zone[MonitorId]=" + str(lista[i])+ "\\"
	print "&Zone[Type]=Active\\"
	print "&Zone[Units]=Percent\\"
	print "&Zone[NumCoords]=4\\"
	print "&Zone[Coords]=0,0 1279,0 1279,719 0,719\\"
	print "&Zone[Area]=921600\\"
	print "&Zone[AlarmRGB]=16711680\\"
	print "&Zone[CheckMethod]=Blobs\\"
	print "&Zone[MinPixelThreshold]=25\\"
	print "&Zone[MaxPixelThreshold]=\\"
	print "&Zone[MinAlarmPixels]=27648\\"
	print "&Zone[MaxAlarmPixels]=691200\\"
	print "&Zone[FilterX]=3\\"
	print "&Zone[FilterY]=3\\"
	print "&Zone[MinFilterPixels]=27648\\"
	print "&Zone[MaxFilterPixels]=691200\\"
	print "&Zone[MinBlobPixels]=18432\\"
	print "&Zone[MaxBlobPixels]=\\"
	print "&Zone[MinBlobs]=1\\"
	print "&Zone[MaxBlobs]=\\"
	print "&Zone[OverloadFrames]=0\""
	print "\n"



