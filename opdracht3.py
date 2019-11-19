# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:11:46 2019

@author: schoc
"""
import os 
os.chdir("G:/home/informatical/project")

import infofun 


def decodeer_bin_T_seq(bin_getal):
    gedecodeerd_bin_getal = ""
    for i in range(len(bin_getal)//3): 
        gedecodeerd_bin_getal +=  str(int(bin_getal[3*i:3*i+3], base=2)) 
    return gedecodeerd_bin_getal 
