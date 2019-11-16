# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:26:35 2019

@author: schoc
"""

def codeer_T_seq(temp): 
    sequentie= ""
    n = 0 
    
    for n in temp:
        if 0 <= float(n) <= 79 :
            getal = float(n) / 10 
            getal = int(getal)
            getal = str(getal)
            sequentie = sequentie + getal 
    
    for i in sequentie: 
        i = int(i)
        binair = '{0:03b}'.format(i)
        print(binair, end="")
        
    return binair 

temp= [12.1, 43.5, 61.9]
temperatuur = codeer_T_seq(temp)
