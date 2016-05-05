#!/usr/bin/python
from __future__ import division
from collections import defaultdict
import dircache
import time
import os
import inspect

path_train = os.path.dirname(os.path.abspath(
							inspect.getfile(
							inspect.currentframe()))) + "/training/"
path_test = os.path.dirname(os.path.abspath(
							inspect.getfile(
							inspect.currentframe()))) + "/attack/"

def buildTree(systemCalls, decisionTree):
	parts = systemCalls.split(' ',1)
	if len(parts) == 1: 
		decisionTree['ENDKEY'].append(parts[0])
	else:
		node, remainingCalls = parts
		if node not in decisionTree:
			decisionTree[node] = defaultdict(dict, (('ENDKEY', []),))
		buildTree(remainingCalls, decisionTree[node])

def checkTree(systemCalls, decisionTree):
	parts = systemCalls.split(' ',1)
	if len(parts) == 1:
		return False
	else:
		node, remainingCalls = parts
		if node not in decisionTree:
			return True
		else:
			checkTree(remainingCalls, decisionTree[node])

fileList = dircache.listdir(path_train)
trainingTree = defaultdict(dict,(('ENDKEY', []),))
for fileName in fileList:
	f = open(path_train + fileName,'r')
	systemTrace = f.readline()
	buildTree(systemTrace, trainingTree)
	f.close

folderList = dircache.listdir(path_test)
for folderName in folderList:
	fileList = dircache.listdir(path_test + '/' + folderName)
	normal = attacks = 0
	for fileName in fileList:
		f = open(path_test + '/' + folderName + '/' + fileName,'r')
		systemTrace = f.readline()
		f.close
		val = checkTree(systemTrace, trainingTree)
		if val is True:
			attacks +=1 
		else: 
			normal += 1
	if attacks > 0:
		percent = attacks / len(fileList)
		print ("Attack vector found in " + folderName + 
				" at " + str(percent*100) + " %")

