#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:07:37 2018

@author: yuktigoswami
"""

def sumprimes(n):
    s=0
    
    for i in n:
      if(i>1): 
       a=0
       for j in range(1,i):
         if(i%j==0 and j!=1 ):
             a=a+1
       if(a<1):
           s=s+i
    if(s>0):
        return(s)
    else:
        return(0)
           
print(sumprimes([-3,1,6]))