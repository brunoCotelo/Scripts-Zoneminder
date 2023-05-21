# -*- coding: utf-8 -*-

#Lê um arquivo com a lista dos IDs de monitores com quebra de linha a cada um gerados pelo id_colect.py e copia para uma lista
arquivo = open("ids.txt")
list = arquivo.read()
arquivo.close()

#Quebra a lista em elementos separados por \n, restando em apenas os IDs unicos na lista
list = list.split("\n")

#Faz um loop para gerar os comandos curl necessarios para alterar algum parametro especifico, identificado por estar entre chaves e com seu valor após o "="
for i in range(len(list)):
	print "\ncurl -XPOST http://localhost/zm/api/monitors/" + list[i] + ".json -d \"Monitor[Function]=Record\""