#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:57:57 2018

@author: yuktigoswami
"""

# to find the number of primes in the list
l=[3,3,4,3,2,4,5,7,9,12,4,24,65]
for i in l:
       p=0
       for j in range (2,i):
              if i%j==0:
                     p=p+1
       if p<1:
              print("number ",i," is prime")