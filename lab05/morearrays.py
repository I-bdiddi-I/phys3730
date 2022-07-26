#!/usr/plocal/bin/python3
import numpy as np

A = np.array([[0,3,-1],[9,0,1]])
print('A =',A)
print('method 2:')
for a in A:
    print(a)
print('method 3:')
for a in zip(A):
    print(a)

print('A[:,0] =',A[:,0])
print('A[1,:] =',A[1,:])
print('A[:,:] =',A[:,:])

x = A[0,:] = np.where(A[0,:]>-2,-99,A[0,:])
y = A[1,:] = np.array([1,2,3])
print('A[0,:] = np.where(A[0,:]>-2,-99,A[0,:]):',x)
print('A[1,:] = np.array([1,2,3]):',y)
print('A =',A)

x = A+A
print('x = A+A:',x)
x = x/4
print('x = x/4:',x)
x *= 10
print('x *= 10:',x)

Z=np.zeros((4,4))
print('Z =',Z)
O=np.ones((4,4))
print('O =',O)
D=np.diag(np.ones(4))
print('D =',D)

B = np.linspace(0,15,16)
B = B.reshape((4,4))
print('B =',B)

x=np.sum(D)
print('np.sum(D) =',x)
y=np.dot(O,B)
print('np.dot(O,B) =',y)
g=B.T
print('B.T =',g)

n = 4
print('n =',n)
x = np.linspace(0,n-1,n)
print('x = np.linspace(0,n-1,n):',x)
y = np.linspace(0,n-1,n)
print('y = np.linspace(0,n-1,n):',y)
X,Y = np.meshgrid(x,y)
print('X,Y = np.meshgrid(x,y):',X,Y)
print('X =',X)
print('Y =',Y)

print('X.shape:',X.shape)
