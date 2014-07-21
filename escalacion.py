#!/usr/bin/python
#coding=UTF-8
def main():
	print 'IPC este a�o'
	ipc1=float(float(raw_input()))
	ipc=1+(float(ipc1/100))
	
	print 'ETCL este a�o'
	etc1=float(raw_input())
	print 'ETCL a�o anterior'
	etc2=float(raw_input())
	etcl=float(etc1)/float(etc2)
		
	print 'Division 28 este a�o'
	mo281=float(raw_input())
	print 'Division 28 an�o anterior'
	mo282=float(raw_input())
	print 'Division 30 este a�o'
	mo301=float(raw_input())
	print 'Division 30 a�o anterior'
	mo302=float(raw_input())
	ipri=0.5*(float(mo281)/float(mo282))+0.5*((float(mo301)/float(mo302)))
	
	print '\n--------------------------------------------------------'
	print 'Indice de Precios de Consumo (IPC): ',ipc
	print 'Mano de Obra (MO): ',etcl
	print 'Materia Prima (MP): ',ipri
	P= (0.057 + 0.750*(etcl) + 0.061*(ipc) + 0.132*(ipri))
	print  'Escalacion (P) del ejercicio es: ', P
	print '--------------------------------------------------------\n'

if __name__=='__main__':
	main()
