import numpy
import sys

g =numpy.array([[1,0,0,0,1,1,0],[0,1,0,0,1,0,1],[0,0,1,0,0,1,1 ],[0,0,0,1,1,1,1]])
s =numpy.array([[1,1,0,1],[1,0,0,1],[0,1,1,1],[1,1,0,0]])
p=numpy.array([[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,1],[1,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0]])	

print('G:\n',g)
print('S:\n',s)
print('P:\n',p)


matrix = numpy.dot(s,g)%2
G_1 = numpy.dot(matrix,p)%2

print('Result:\n',G_1)

message = ([1,1,0,1])
e = ([0,0,0,0,1,0,0])

res=numpy.dot(message,G_1)%2

cipher = numpy.add(res,e)%2

print('\nCipher:',cipher)

p_1=numpy.linalg.inv(p)%2

print('\nP^{-1}:\n',p_1)

y_1 = numpy.dot(cipher,p_1)%2

print("\ny\':",y_1)

s_1=numpy.linalg.inv(s)%2

print ('\nS^{-1}:\n',s_1)

syn = ([1,0,0,0])

decipher = numpy.dot(syn,s_1)%2

print ('\nDecipher:',decipher)
