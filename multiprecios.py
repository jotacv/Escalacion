#!/usr/bin/python
#coding=UTF-8
# Written by: jotacv
# email: jotacv@hotmail.es

import sys
def main():
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
	for key in dic.keys():
		print key,
		for key2 in dic[key]:
			print "\t"+key2+"\t"+str(dic[key][key2])

if __name__ == "__main__":
	main()
