#!/usr/plocal/bin/python3

import numpy as np

n = 10
x = np.zeros(n)
print('n =',n)
print('np.zeros(n) =',x)
print('x[0] =',x[0])
print('len(x) =',len(x))

x = np.arange(1,n+1)
print('np.arange(1,n+1):',x)

x = np.linspace(1,n,n)
print('np.linespace(1,n,n):',x)

print('x[-1] =',x[-1])
print('x[2:4] =',x[2:4])
print('x[8:] =',x[8:])
print('x[::-1] =',x[::-1])
print('x[::2] =',x[::2])

print('len(x) =',len(x))
print('x.size =',x.size)
print('x.shape =',x.shape)
print('np.sum(x) =',np.sum(x))
print('np.sin(x) =',np.sin(x))
print('np.exp(-0.5*x**2) =',np.exp(-0.5*x**2))
print('np.abs(x) =',np.abs(x))
print('np.sum(x)-np.abs(x)',np.sum(x)-np.abs(x))

g=x[x>4.5]
print('g = x[x>4.5] =',g)
print('len(g):',len(g))
x = np.where(x>4.5,-99,x)
print('np.where(x>4.5,-99,x) =',x)

x = np.linspace(n/2,n,len(x[x==-99]))
#g = np.where(x==-99,x+99+n,x)
print('x = np.linspace(n/2,n,len(x[x==-99])):',x)
#this would be our final state of x. I tried figuring out a way to convert the
#previous array back into the increaing array from x=1 to x=10, but I couldn't
#figure it out using the method recommended in the lab.

x = np.linspace(1.0,10.0,10)
y = x
y = np.where(x>n-1,-99,x)
print('x =',x)
print('y = np.where(x>n-1,-99,x):',y)

y = np.where(y==-99,n,y)
print('y = np.where(y==-99,n,y):',y)
y = np.copy(x)
print('y = np.copy(x):',y)
y = np.where(y<7,12+y,y)
print('x =',x)
print('y = np.where(y<7,12+y,y):',y)
y = np.sin(x)+2
print('y = np.sin(x)+2:',y)
