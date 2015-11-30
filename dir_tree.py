# -*- coding: utf-8 -*-
#_author_ = flouthoc (http://github.com/flouthoc)
import os
def rec_tree(path, append, string=""):
	CYAN='\033[94m'
	WHITE='\033[1;37m'
	f=""
	point1 = "──"
	point = append + '├' + point1
	files = [f for f in os.listdir(path) if os.path.isfile(path+'/'+f)]
	
	if(append == ""):
		append = '   '

	append += '   '

	for x in files:
		print "%s%s" %(point, x)

	directory = [f for f in os.listdir(path) if os.path.isdir(path+'/'+f)]
	for x in directory:
		point = point.replace('├', '└')
		print "%s%s%s%s" %(point, CYAN, x, WHITE)
		rec_tree(path+'/'+x, append, string)
	

rec_tree('.', "")
	
