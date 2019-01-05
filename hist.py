#!/bin/python
import numpy as np
import math

maxdata = 0;
mindata = 100000000000000;
dataset = []
f = open("list.log", 'r')
for line in f:
  for data in line.split(','):
    if(data == ''):
      continue
    if(float(data) < mindata and float(data) > 0):
      mindata = float(data)
    if(float(data) > maxdata):
      maxdata = float(data)
    dataset += [float(data)]

N = 5000
results = [0]*N
zero = 0
for data in dataset:
  if(data == 0):
    zero += 1
    continue
  if(data == maxdata):
    continue
  idx =  math.floor( (data - mindata) / ((maxdata - mindata)/N) )
  if(idx < 0):
    print data
  #print( data, mindata + ((maxdata - mindata)/N)*idx, mindata + ((maxdata - mindata)/N)*(idx+1) )
  if(int(idx) >= N):
    print (data, (data - mindata) / ((maxdata - mindata)/N) )
  results[int(idx)] += 1;
for i in range(0,N):
  print results[i],
print ""
print zero
print (mindata, maxdata)
print len(dataset)
