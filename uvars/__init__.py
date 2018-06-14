version = "0.0.2"

import os
from uvars.variables import *

def readfile(tgtdict, path):
	with open(path) as of:
		lines = of.readlines()
		for idx, l in enumerate(lines):
			splt = l.split()
			if len(splt) != 2:
				raise Exception("File format error. (file:{}, line:{})".format(path, idx))
			if splt[0] in tgtdict:
				raise Exception("Repeated key. (file:{}, key:{}, line:{})".format(path, splt[0], idx))	
			tgtdict[splt[0]] = splt[1]

udict = {}
udirs = {}

if os.path.exists(ufilepath): 
	readfile(udict, ufilepath)

if os.path.exists(udirpath): 
	for f in os.listdir(udirpath):
		udirs[f] = {}	
		readfile(udirs[f], os.path.join(udirpath, f))

print(udict)
print(udirs)