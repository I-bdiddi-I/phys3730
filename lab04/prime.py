#!/usr/plocal/bin/python3

import math as m
import numpy as np

print('Prime numbers smaller than or equal to 1000:')

for number in range(1,1001):
    if number > 1:
        for i in range (2,number):
            if (number %i)==0:
                break
        else:
            print(number)
