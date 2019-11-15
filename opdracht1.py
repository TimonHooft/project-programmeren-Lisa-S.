# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:34:01 2019

@author: schoc
"""

sequentie = "" 

while True: 
    temperatuur = input("Geef een temperatuur: ")
    if temperatuur == "STOP": 
        break 
    if 0 <= float(temperatuur) <= 79 :
        getal = float(temperatuur) / 10 
        getal = int(getal)
        getal = str(getal)
        sequentie = sequentie + getal 

print(" De sequentie is ", sequentie)
