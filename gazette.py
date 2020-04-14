import os
import requests

file = open("read.txt","w")
file.write("<div '=postion' <span>98889898</span>"+ "\n")
file.write("<div '=postion' <span>98889898</span>"+ "\n")
file.write("<div '=postion' <span>98889898</span>"+ "\n")
file.close()
#data = []
files= open("read.txt","r")
for file in files:
    data = file.read()
words = data.split()
print(words[0])
#for file in files:
#    data.append(file)
#print(data)