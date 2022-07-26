#!/usr/plocal/bin/python3
i = 3; j = 1.0
x = 1.235e45; z = 1.23+4.56j
s = '1.234e45'
print('i: val, type:',i,type(i))
print('j: val, type:',j,type(j))
print('i*2: val, type:',i*2,type(i*2))
print('i/2: val, type:',i/2,type(i/2))
print('i//2: val, type:',i//2,type(i//2))
print('z**2: val, type:',z**2,type(z**2))
print('z*x: val, type:',z*x,type(z*x))

print('casting x =',x,'to str, int:',str(x),int(x));
print('int(1/2) =',int(1/2))

xno = 1.23*10**34     # a way to assign a big float
xyes = 1.23e34        # but always use scientific notation!
xbig = 1e+308         # try! 
xtoobig = 1e+309      # and try this!
xlargest = 1.999999999*(2**1023)
print('xno,xyes,xbig,xtoobig,xlargest:',xno,xyes,xbig,xtoobig,xlargest)
# Answer 1: you can only print values smaller than 2**1024 because anything
# larger goes beyond the capabilites of the 64-bit code (binary) python runs on.

x = 0.123456789012345678901234567890
print('x w/lots of sig figs:',x)
# Answer 2: about 17

ibig = 2**1000
print('ibig(1):',ibig)
print('ibig(1)/2:',ibig/2)
print('ibig(1)//2:',ibig//2)

ibig = 2**2000
# print(ibig/2)
# Answer 3: we have an OverflowError meaning that the integer division result is
# too large for a float. 2**2000/2 would give us a value of 2**1999 which is >
# the 2**1024 that the computer can compute.
print('ibig(2)//2:',ibig//2)

ibig = 2**20
print('ibig(3):',ibig)        # standard print, for a "baseline"  
print("f'{ibig(3):b}':",f'{ibig:b}') # pre-python3.6, try
print("'{0:b}'.format(ibig):",'{0:b}'.format(ibig))
print("f'{ibig(3):f}':",f'{ibig:f}')
print("f'{ibig(3):e}':",f'{ibig:e}')
print("f'{ibig(3):g}':",f'{ibig:g}')

import math as m
import numpy as np

theta = 1.234;
ym = m.sin(theta)
yn = np.sin(theta)
xn = np.cos(theta)
z = np.sqrt(xn**2+yn**2)

print('theta =',theta)
print('ym = m.sin(theta):',ym)
print('yn = np.sin(theta):',yn)
print('xn = np.cos(theta):',xn)
print('z = np.sqrt(xn**2+yn**2):',z)

print('9.87*10**(-6):',9.87*10**(-6))
print('9.87e-6:',9.87e-6)
print('sin(1.2345):',np.sin(1.2345))
print('exp(-(1.2345)**2.5):',np.exp(-(1.2345)**2.5))
print('pi:',np.pi)
