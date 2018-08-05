import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product, combinations
import csv
import sys
from TensionRigFunctions.TensionRigFunctions import readers as rdr

rdr=rdr()

toprint=rdr.TensionReader(file=r'C:\Users\eivinhug\NTNU\PhD\Testing\RigFiles_18042018_2\B26.txt')

print(toprint)