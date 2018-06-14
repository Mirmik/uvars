version = "0.0.2"

import os
import uvars.variables

files = []
if os.path.exists(uvars.variables.uvarsfile): files.append(uvars.variables.uvarsfile)
if os.path.exists(uvars.variables.uvarsdirectory): files.extend([os.path.join(uvars.variables.uvarsdirectory, f) for f in os.listdir(uvars.variables.uvarsdirectory)])

uvarsdict = {}
for f in files:
	with open(f) as of:
		lines = of.readlines()
		for idx, l in enumerate(lines):
			splt = l.split()
			if len(splt) != 2:
				print("File format error. (file:{}, line:{})".format(f, idx))
				exit(-1)
			uvarsdict[splt[0]] = splt[1]

def getdict():
	return uvarsdict

def get(key):
	return uvarsdict[key]