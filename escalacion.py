#!/usr/bin/python
#coding=UTF-8
# Written by: jotacv
# email: jotacv@hotmail.es

'''
Para el Incremento de la Mano de Obra (ETCL):
	1.- Ir a: http://www.ine.es/daco/daco42/etcl/etcl[*q][*y].pdf
		sustituyendo [*q] por el trimestre que se desee y [*y] por el año que se desee.
		Ejemplo: http://www.ine.es/daco/daco42/etcl/etcl0411.pdf corresponde al cuarto cuatrimestre del año 2011.
	2.- Encontraremos los datos en la pagina 5 del pdf, en la tabla 1 de resultados nacionales, columna del coste laboral 			por hora efectiva en euros (cuarta columna numerica),fila Industria (segunda fila).
		En el ejemplo anterior: 22.46.

Para el Incremento de Materia Prima (IPC):
	1.- Ir a: http://www.ine.es/daco/daco42/daco421/ipc12[*y].pdf
		sustituyendo [*m] por el mes que se desee [*y] por el año que se desee.
		Ejemplo:http://www.ine.es/daco/daco42/daco421/ipc1210.pdf corresponde a Diciembre del año 2010.
		[!!]Si queremos conocer los datos anuales ingresaremos siempre el mes de Diciembre (12).
	2.- Encontraremos los datos en la primera pagina, en la tabla Indice General, en la columna Variacion Interanual 			(tercera columna numerica).
		En el ejemplo anterior: 3,0.

Para el Incremento del Termino Fijo(IPRI):
	1.- Ir a: http://www.ine.es/daco/daco42/daco423/ipri[*m][*y].pdf
		sustituyendo [*m] por el mes que se desee y [*y] por el año que se desee.
		Ejemplo:http://www.ine.es/daco/daco42/daco423/ipri0112.pdf corresponde a Enero del año 2012.
		[!!]Si queremos conocer los datos anuales ingresaremos siempre el mes de Diciembre (12).
	2.- Encontraremos los datos en la pagina cuatro, filas "Fabricación de maquinaria y equipo n.c.o.p" y 			"Fabricación de otro material de transporte",columna "Indice".
		En el ejemplo anterior: 113.5 y 105.2.
'''

import subprocess, sys, time, os

ectl='http://www.ine.es/daco/daco42/etcl/etcl'
ipc='http://www.ine.es/daco/daco42/daco421/ipc'
ipri='http://www.ine.es/daco/daco42/daco423/ipri'
months=('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
trims=('Primer trimestre','Segundo trimestre','Tercer trimestre','Cuarto trimestre')

def Exit(year):
	print 'No se han encontrado datos relativos al año '+str(year)
	sys.exit('Data Error')

def ParseFile(fname):
	if fname[:4] !='ipri':
		print 'Introduzca el valor: ',
		sb=subprocess.Popen(['evince',fname],stdout=open('/dev/null'),stderr=open('/dev/null'))
		sys.stdout.flush()
		v=raw_input().replace(',','.')
		sb=subprocess.Popen(['kill',str(sb.pid)])
	else:
		v=(0,0)
		print 'Introduzca los valores:'
		sb=subprocess.Popen(['evince',fname],stdout=open('/dev/null'),stderr=open('/dev/null'))
		print '    Division 28: Fabricacion de maquinaria y equipo mecanico: ',
		sys.stdout.flush()
		v0=raw_input().replace(',','.')
		print '    Division 30: Fabricacion de otro material de transporte: ',
		sys.stdout.flush()
		v1=raw_input().replace(',','.')
		v=(v0,v1)
		sb=subprocess.Popen(['kill',str(sb.pid)])
	return v

def PrintData(y1, y2):
	etcl=float(y1.etcl)/float(y2.etcl)
	ipri=0.5*(float(y1.ipri[0])/float(y2.ipri[0]))+0.5*((float(y1.ipri[1])/float(y2.ipri[1])))
	ipc=1+(float(y1.ipc)/100)
	print '\n--------------------------------------------------------'
	print 'Indice de Precios de Consumo (IPC): ',ipc
	print 'Mano de Obra (MO): ',etcl
	print 'Materia Prima (MP): ',ipri
	P= (0.057 + 0.750*(etcl) + 0.061*(ipc) + 0.132*(ipri))
	print  'Escalacion (P) del ejercicio ',y1.year,' es: ', P
	print 'Incremento de precios: ',(P-1)*100
	print '--------------------------------------------------------\n'

	
class YearData():
	def __init__(self,y):
		self.year=y
		self.etcl=0
		self.ipc=0
		self.ipri=(0,0)
		
	def __get(self,typ):
		errlst=months
		if typ=='etcl': 
			mode=ectl
			aux=4
			errlst=trims
		elif typ=='ipc': 
			mode=ipc
			aux=12
		elif typ=='ipri': 
			mode=ipri
			aux=12
		ok=False
		yr=str(self.year)[-2:]
		while not ok:
			print typ+': Obteniendo '+errlst[aux-1]+' de '+str(self.year),
			sys.stdout.flush()
			aux_str=str(aux)
			if len(aux_str)==1: aux_str='0'+aux_str
			st=os.system('wget ' + mode + aux_str + yr +'.pdf -H -nd -r -A ".pdf" 2>/dev/null')
			if st==0:
				ok =True
			else:
				aux-=1
				if aux==0:
					Exit(self.year)
				print ' no disponible.'
		aux_value=ParseFile(typ+aux_str+yr+'.pdf')
		sb=subprocess.Popen(['rm',typ+aux_str+yr+'.pdf'])
		if typ=='etcl': self.etcl=aux_value
		elif typ=='ipc': self.ipc=aux_value
		elif typ=='ipri': self.ipri=aux_value
		
	def get_data(self):
		print
		self.__get('etcl')
		self.__get('ipc')
		self.__get('ipri')
		print	

def main():
	print 'Introduzca el año: ',
	y1=YearData(int(raw_input()))
	y2=YearData(y1.year-1)
	y1.get_data()
	y2.get_data()
	PrintData(y1,y2)
			

if __name__=='__main__':
	main()
