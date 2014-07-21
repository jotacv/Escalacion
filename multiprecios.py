#!/usr/bin/python
#coding=UTF-8
# Written by: jotacv
# email: jotacv@hotmail.es

import sys
def main():
	if len(sys.argv)==3:
		lst=open(sys.argv[1]).read().split('\n')
		dic={}
		for line in lst[:-1]:
			tp = line.split('\t')
			if tp[0] in dic.keys():
				if tp[1] in dic[tp[0]].keys():
					dic[tp[0]][tp[1]]+=1
				else:
					dic[tp[0]][tp[1]]=1
			else:
				dic[tp[0]]={}
				dic[tp[0]][tp[1]]=1
		
		outp=open(sys.argv[2],'w')
		for key in dic.keys():
			outp.write(key)
			for key2 in dic[key]:
				outp.write("\t"+key2+"\t"+str(dic[key][key2])+"\n")
	else:
		print "python multiprecios.py [fichero_entrada] [fichero_salida]"
		print "[fichero_entrada] debe ser un fichero que exista consistente en un listado de dos columnas separadas por un tabulador. NO DEBE ACABAR EN UN SALTO DE LINEA"
		print "Ejemplo: J57151717-904	1730.1421818097"
		print "Los datos quedan agrupados segun el part-number en la columna izquierda y bajo el en la columna derecha los precios asociados con ese part number y su cantidad"

if __name__ == "__main__":
	main()
