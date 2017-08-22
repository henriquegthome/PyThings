#!/usr/bin/python3
import sys
z = str(input("Matrix size (e.g. '4x3', '2x4')\n"))
try:
	xy = z.split("x"); x = int(xy[1]); y = int(xy[0])
except:
	print ("(err:01)Invalid Format."); sys.exit(0)
null_matrix = 0; diagonalORidentity= 0; identity_check = 0
matrix = [[0 for i in range(x)] for n in range(y)]
for i in range(y):
	for n in range(x):
		matrix[i][n] = int(input("Input value for a%i%i: " % (i + 1, n + 1)))
		null_matrix = null_matrix + matrix[i][n]
		if i != n:
			diagonalORidentity = diagonalORidentity + matrix[i][n]
		if i == n:
			identity_check = identity_check + matrix[i][n]
if int(y) == 1:
	print ("Line matrix.\n")
if int(x) == 1:
	print ("Column matrix.\n")
if null_matrix == 0:
	print ("Null matrix.\n")
if int(x) == int(y):
	print ("Square matrix.\n")
if diagonalORidentity == 0:
	if identity_check / int(x) == 1:
		print ("Identity matrix.\n")
	elif null_matrix != 0:
		print ("Diagonal matrix.\n")
print("Final matrix:\n")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))
