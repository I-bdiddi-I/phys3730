#!/usr/plocal/bin/python3


A = [ 0, 1, 3, 5, 7, 11, 13]
print('A =',A)
print('second method:')
for a in A:
    print(a)

B = [z**2 for z in A]
print('B =',B)
[print(b) for b in B]

print('the first 4 elements of A:', A[:4])

print('the last element:', A[-1])

print('the length of A/# of elements:', len(A))

print('every other element starting with the 0th (leading) elelment:', A[0:len(A):2])

print('A in reverse order:', A[::-1])

print('A+A =', A+A)

print('A*2 =', A*2)

X,Y,ID = [0,1,2],[-1,0,1],['A','B','C']
print('X =',X)
print('Y =',Y)
print('ID =',ID)
print('zip(X,Y) =',zip(X,Y))
for x,y,i in zip(X,Y,ID):
    print(x,y,i)

r = [3,1,4,1,5,9]
print('r =',r)
print('enumerate(r):', enumerate(r))
print('list(enuerate(r)):',list(enumerate(r)))
print('printing i,rel in enumerate(r)')
p = []
for i,rel in enumerate(r):
    print(i,rel)
    p.append(r[i]**i)

print('p[i] =',p)

trans={'bikes':4, 'scooters':2, 'mopeds':3}

print('trans =',trans)
print('trans.items() =',trans.items())

for key,val in trans.items():
    print('We have',val,key)
