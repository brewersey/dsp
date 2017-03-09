# Matrix Algebra

#Impost NUMPY for matrix math
import numpy as np

#Create matrices
A = np.array([[1, 2, 3], [2, 7, 4]])

B = np.array([[1, -1], [0, 1]])

C = np.array([[5, -1], [9, 1], [6,0]])

D = np.array([[3, -2, -1], [1, 2, 3]])

u = np.array([6, 2, -3, 5])

v = np.array([3, 5, -1, 4])

w = np.array([1, 8, 0, 5])
w = np.transpose(w) 

a = 6

#1 Print matrices & dimensions
print(A)
print(A.shape)
#[[1 2 3]
#[2 7 4]]
#(2, 3)

print(B)
print(B.shape)
#[[ 1 -1]
#[ 0  1]]
#(2, 2)

print(C)
print(C.shape)
#[[ 5 -1]
#[ 9  1]
#[ 6  0]]
#(3, 2)

print(D)
print(D.shape)
#[[ 3 -2 -1]
# [ 1  2  3]]
#(2, 3)

print(u)
print(u.shape)
#[ 6  2 -3  5]
#(4,)

print(v)
print(v.shape)
#[ 3  5 -1  4]
#(4,)

print(w)
print(w.shape)
#[1 8 0 5]
#(4,)

#2 Print vector operations
print(u + v)
#[ 9  7 -4  9]

print(u - v)
#[ 3 -3 -2  1]

print(a*u)
#[ 36  12 -18  30]

print(np.sum(u*v))
#51

us = np.sum(np.square(u))
us = np.sqrt(us)
print(us)
#8.60232526704

#3 Print matrix operations
try:
    print(A + C)
except:
    print('not defined')
#not defined

try:
    print(A - np.transpose(C))
except:
    print('not defined')
#[[-4 -7 -3]
#[ 3  6  4]]
 
try:
    print(np.transpose(C) + 3*D)
except:
    print('not defined')
#[[14  3  3]
#[ 2  7  9]]

try:
    print(np.dot(B, A))
except:
    print('not defined')
#[[-1 -5 -1]
#[ 2  7  4]]

try:
    print(np.dot(B, np.transpose(A)))
except:
    print('not defined')
#not defined

#Optional
try:
    print(np.dot(B, C))
except:
    print('not defined')
#not defined

try:
    print(np.dot(C, B))
except:
    print('not defined')
#[[ 5 -6]
#[ 9 -8]
#[ 6 -6]]

try:
    print(np.dot(B, B))
except:
    print('not defined')
#[[ 1 -2]
#[ 0  1]]

try:
    print(np.dot(A, np.transpose(A)))
except:
    print('not defined')
#[[14 28]
#[28 69]]

try:
    print(np.dot(np.transpose(D), D))
except:
    print('not defined')
#[[10 -4  0]
#[-4  8  8]
#[ 0  8 10]]    
