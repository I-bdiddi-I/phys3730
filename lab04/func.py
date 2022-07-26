#!/usr/plocal/bin/python3
def cuberoot(x):
    y = x**(1.0/3.0)
    return y

x = 1000.0
y = cuberoot(x)
print('method 1: x,(x)^1/3:',x,',',y)

x = 24.0
y = cuberoot(x)
print('method 1: x,(x)^1/3:',x,',',y)

x = 168.0
y = cuberoot(x)
print('method 1: x,(x)^1/3:',x,',',y)

def cuberootx():
    y = x**(1./3.)
    return y

x = 1000.0
y = cuberootx()
print('method 2: x,(x)^1/3:',x,',',y)

def CubeRootX():
    global x
    x = x**(1./3.)
    return

x = 1000.0
print('method 3: x:',x)
CubeRootX()
print('method 3: (x)^1/3:',x)
