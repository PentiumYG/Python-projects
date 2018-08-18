#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:59:09 2018

@author: yuktigoswami
"""

list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
a=int(input())
out = 0
for item in list_1:
    if(item%a==0 and item!=a):
        out=out+1
    
print(out)    
