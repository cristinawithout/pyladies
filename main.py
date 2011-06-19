#!/bin/python
import sets,random
import re

myfile = open("bigfile.txt", "r")
myset = set()

for line in myfile:
  for word in line.split():
    myset.add(word)

mylist = list(myset)

newlist = [];
for x in mylist:
  myword = re.sub("[^a-zA-Z']","",x)
  if len(myword) > 2 and len(myword) < 10:
    newlist.append(myword);

#print newlist;
print "How many words? ",
num = int(raw_input())
for x in range(0,num):
 print( newlist[random.randint(0,len(newlist)-1)]),
