import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import csv
import sys
from TensionRigFunctions.TensionRigFunctions import readers as rdr

rdr=rdr()

toprint=rdr.TensionReaderMTS(file=r'C:\Users\eivinhug\OneDrive - NTNU\PhD_Backup\NTNU\PhD\Testing\Laminate_E\TestRig_Files\E07-14092018 09-14-18 18 00 39\E07_14092018.txt')
print(len(toprint[0]))

print(type(toprint[0][0]))
print(toprint[0][0])

print(min(toprint[1]))
print("Fmin",min(toprint[1]))
plt.plot(toprint[1],toprint[0])
plt.show()