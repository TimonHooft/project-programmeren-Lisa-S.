# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:49:48 2019

@author: schoc
"""

def codeer_T_seq_PB(temp): 
    sequentie=""
    n = 0 
    enenteller = 0 
    
    
    n= 0 
    for n in temp:
        if 0 <= float(n) <= 79 :
            getal = float(n) / 10 
            getal = int(getal)
            getal = str(getal)
            sequentie = sequentie + getal 
            
    for i in sequentie: 
        i = int(i)
        binair = '{0:03b}'.format(i)
        #print(binair, end="")
        
    n=0
    for n in binair : 
        if n == "1"  :
            enenteller= enenteller + 1 
            #print(enenteller)
            
    if enenteller % 2 == 0 : 
        binair = "0" + binair
       # print("voeg 0 vanvoor toe")
        
    else: 
        binair = "1" + binair 
        #print("voeg 1 vanvoor toe")
    
    return binair  

print(codeer_T_seq_PB([12.1]))

#werkt enkel voor 1 getal, niet voor volledige lijst 



