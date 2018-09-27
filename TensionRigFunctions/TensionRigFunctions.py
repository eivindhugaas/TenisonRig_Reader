import numpy as np
import pandas as pd
import math
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import csv
import sys
from os import listdir
from os.path import isfile, join
from scipy.signal import savgol_filter
import pickle
plt.rcParams.update({'font.size': 30})
class readers:
    def __init__(self):
        Check="OK"

    def TensionReader(self,file='C:\file\you\wish\to\open.txt'):
        '''
        Takes one tensionrig.txt file, reads it and returns the 
        "Points" , "Elapse Time" , "Scan Time" , "Load" , "Disp" , "Axial1_Cmd" , "" , "Seconds" , "Seconds" , "kN" , "mm" , "kN"
        1        ,   0.0000      ,    0.0000   ,  4.994 , -59.04 , 5.001 ,        
        '''
        
        f  = open(file, 'r') 
        start=['Points','Elapse Time','Scan Time','Load','Disp','Axial1_Cmd','\n']
        Lines=[]
        n=0
        with f as oldfile, open('newfile.txt', 'w') as newfile:
            for d in range(len(start)):
                newfile.write(start[d]) 
                if d!=len(start)-1:
                    newfile.write('\t')
            for line in oldfile:
                #if num(line[0]) is num
                #if not any(bad_word in line for bad_word in bad_words):
                if 'Axial1' not in line and 'Points' not in line and 'Seconds' not in line and file not in line and 'Movers' not in line and 'kN' not in line and 'Movers' not in line and 'Units' not in line and 'Channels' not in line and 'Load' not in line and 'Created' not in line and 'Exported' not in line:# and '\n' not in line:    
                    if line.strip():
                        dline=line.split('\t')
                        print(dline)
                        n=n+1
                        dline[0]=n
                        for i in range(len(dline)):
                            
                            newfile.write(str(dline[i]))
                            
                            if i!=len(dline)-1:
                                newfile.write('\t')
                                Lines.append(dline[i])
        
        

        return Lines
    
    
    def TensionReaderMTS(self,file='C:\file\you\wish\to\open.txt'):
        '''
        Takes one tensionrig.txt file, reads it and returns the 
        "Points" , "Elapse Time" , "Scan Time" , "Load" , "Disp" , "Axial1_Cmd" , "" , "Seconds" , "Seconds" , "kN" , "mm" , "kN"
        1        ,   0.0000      ,    0.0000   ,  4.994 , -59.04 , 5.001 ,        
        '''
        
        f  = open(file, 'r') 
        start=['Time','Axial Force','Displacement','\n']
        Lines=[]
        n=0
        Force=[]
        Displacement=[]
        with f as oldfile, open('newfile.txt', 'w') as newfile:
            for d in range(len(start)):
                newfile.write(start[d]) 
                if d!=len(start)-1:
                    newfile.write('\t')
            for line in oldfile:
                #if num(line[0]) is num
                #if not any(bad_word in line for bad_word in bad_words):
                #if 'Axial1' not in line and 'Points' not in line and 'Seconds' not in line and file not in line and 'Movers' not in line and 'kN' not in line and 'Movers' not in line and 'Units' not in line and 'Channels' not in line and 'Load' not in line and 'Created' not in line and 'Exported' not in line:    
                if line.strip():
                    dline=line.split('\t')
                    #print(dline)
                    n=n+1
                    #dline[0]=n
                    for i in range(len(dline)):
                        if n>5:
                            newfile.write(str(dline[i]))
                        
                            if i!=len(dline)-1:
                                newfile.write('\t')
                                Lines.append(dline[i])
                        if n>7:
                            F=float(str(dline[1]).replace(",", "."))
                            D=float(str(dline[0]).replace(",", "."))
                            Force.append(F)
                            
                            Displacement.append(D)
        

        return Force, Displacement