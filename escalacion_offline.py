#!/usr/bin/python
#coding=UTF-8
def main():
	print 'IPC este año'
	ipc1=float(float(raw_input()))
	ipc=1+(float(ipc1/100))
	
	print 'ETCL este año'
	etc1=float(raw_input())
	print 'ETCL año anterior'
	etc2=float(raw_input())
	etcl=float(etc1)/float(etc2)
		
	print 'Division 28 este año'
	mo281=float(raw_input())
	print 'Division 28 anño anterior'
	mo282=float(raw_input())
	print 'Division 30 este año'
	mo301=float(raw_input())
	print 'Division 30 año anterior'
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