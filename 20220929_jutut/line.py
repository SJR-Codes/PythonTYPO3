# -*- coding: cp1252 -*-
filen = "words.txt"

with open(filen) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
	
lines.sort()
for i in lines:
	print(i)