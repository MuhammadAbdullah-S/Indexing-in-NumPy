# accessing elements using indexing
# array[index] # 1d array
# array[row, column] # 2d array

""" navigating through three distinct structural layers 
    using the comma-separated syntax array[matrix, row, column]. 
    Think of a 3D array as a book where you first select the page (matrix), 
    then the line (row), and finally the word (column)
"""

import numpy as np
access_el = np.array([10,20,30,40,50])
print(access_el[0])
print(access_el[1])
print(access_el[2])

access_el_multid = np.array([
    [[10,20,30],[40,50,60]],
    [[70,80,90],[35,65,45]]])
print(access_el_multid, "\n","Dimension of Array:",access_el_multid.ndim)
# accessing elements 
layer1 = access_el_multid[0]
layer2 = access_el_multid[1]
print("Layer1: ",layer1)
print("Layer2: ",layer2)
print()

# Accessing row and columns
layer1Row1 = access_el_multid[0,0]

print("Layer1 Row1: ",layer1Row1)
print("Layer1 Row1 Column1: ", access_el_multid[0,0,0])
print("Layer1 Row1 Column2: ", access_el_multid[0,0,1])
print("Layer1 Row1 Column3: ", access_el_multid[0,0,2])
print()

layer1Row2 = access_el_multid[0,1]
print("Layer1 Row2: ",layer1Row2)
print("Layer1 Row2 Column1: ", layer1Row2[0])
print("Layer1 Row2 Column2: ", layer1Row2[1])
print("Layer1 Row2 Column3: ", layer1Row2[2])
print()

layer2Row1 = access_el_multid[1,0]
print("Layer2 Row1: ", layer2Row1)
print("Layer2 Row1 Column1: ",access_el_multid[1,0,0])
print("Layer2 Row1 Column2: ",access_el_multid[1,0,1])
print("Layer2 Row1 Column3: ",access_el_multid[1,0,2])
print()

layer2Row2 = access_el_multid[1,1]
print("Layer2 Row2 Column1: ", layer2Row2[0])
print("Layer2 Row2 Column2: ", layer2Row2[1])
print("Layer2 Row2 Column3: ", layer2Row2[2])
