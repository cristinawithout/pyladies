#!/bin/python
import sets,random

myfile = open("bigfile.txt", "r")
myset = set()

for line in myfile:
  for word in line.split():
    myset.add(word)

mylist = list(myset)

for x in xrange(0,len(mylist)-1):
 print( mylist[random.randint(0,len(mylist)-1)]),
