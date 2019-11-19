# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:40:05 2019

@author: schoc
"""

sequentie=input("Geef een sequentie: ")
#print(sequentie)

lijst_sequentie = []

for getal in sequentie :
    lijst_sequentie.append(int(getal))
#print(lijst_sequentie)
    
aantal_stijgingen = 0
for i in range(len(lijst_sequentie) - 1): 
    if lijst_sequentie[i + 1] > lijst_sequentie[i]:
         aantal_stijgingen = aantal_stijgingen + 1

print("sequentie: ", sequentie)
print("telt", aantal_stijgingen, "stijgingen")
