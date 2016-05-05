#!/usr/bin/python
from __future__ import division
import dircache
import time
import os
import inspect

trainingPath = os.path.dirname(os.path.abspath(
							inspect.getfile(
							inspect.currentframe()))) + "/training/"
testPath = os.path.dirname(os.path.abspath(
							inspect.getfile(
							inspect.currentframe()))) + "/attack/"

#for each file in training trace directory
fileList = dircache.listdir(trainingPath)
training = []
for fileName in fileList:
	#open the file, split it into system calls, generate clusters
	f = open(trainingPath + fileName,'r')
	systemCalls = f.readline().split( )
	temp = []
	callList = list(set(systemCalls))
	for item in callList:
		callCount = systemCalls.count(item)
		temp.append((item,callCount))
	training.append(temp)
	f.close

folderList = dircache.listdir(testPath)
for folderName in folderList:
	# each directory is a different attack
	validate = []
	fileList = dircache.listdir(testPath + '/' + folderName)
	for fileName in fileList:
		f = open(testPath + '/' + folderName + '/' + fileName,'r')
		systemCalls = f.readline().split( )
		temp = []
		callList = list(set(systemCalls))
		for item in callList:
			callCount = systemCalls.count(item)
			temp.append((item,callCount))
		validate.append(temp)
		f.close

	normal = attacks = 0
	for item in validate:
		try:
			if training.index(item):
				normal += 1
		except:
			attacks += 1
	if attacks > 0:
		percent = attacks / len(validate)
		print ("Attack vector found in " + folderName + 
				" at " + str(percent*100) + " %") 



