#!/usr/plocal/bin/python3

def SieveOfEratosthenes(n):
     
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        if (prime[p] == True):
             
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False

    for p in range(n + 1):
        if prime[p]:
            print (p,end=' ')
 

if __name__=='__main__':
    n = 1000
    print ("Prime numbers smaller", end=' ')
    print ("than or equal to", n)
    SieveOfEratosthenes(n)
