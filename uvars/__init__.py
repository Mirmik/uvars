version = "0.0.2"

import os
import json
from uvars.variables import *

def writedict(dct, path):
	with open(os.path.expanduser(path), 'w') as outfile:
		json.dump(dct, outfile)
	

def readdict(path):
	file = open(os.path.expanduser(path))
	data = json.load(file)
	return data

class context:
	def __init__(self, path = os.path.expanduser(os.getenv("UVARS_PATH", "~/.uvars"))):
		self.path = path
		self.dct = readdict(self.path)

	def setvar(self, var, value):
		tokens = var.split('.')

		n = self.dct
		for l in tokens[:-1]: 
			try:
				n = n[l]
			except:
				n[l] = {}
				n = n[l]

		n[tokens[-1]] = value
		writedict(dct = self.dct, path = self.path)

	def getvar(self, var):		
		tokens = var.split('.')

		n = self.dct
		for l in tokens: 
			n = n[l]
		
		return n

default_context = None

def setvar(var, value):
	global default_context
	if default_context == None:
		default_context = context()
	default_context.setvar(var, value)

def getvar(var):
	global default_context
	if default_context == None:
		default_context = context()
	return default_context.getvar(var)