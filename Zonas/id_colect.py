# -*- coding: utf-8 -*-

#Lê um arquivo com os dados dos monitores ja criados no ZM e copia para uma lista
arquivo = open ("monitors.txt")
lista = arquivo.read()
arquivo.close()

#Quebra a lista resultando apenas nos IDs
lista = lista.split("{\"Id\":\"")

#Faz um loop para escrever na tela os IDs resultantes
for i in range(1,len(lista)):
	print lista[i].split("\"")[0]