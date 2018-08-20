#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:18:14 2018

@author: yuktigoswami
"""

def matched(n):
    p=0
    q=0
    l=[]
    m=[]
    for i in range(0,len(n)): 
        if (n[i]==")" ):
              q=q+1
              l=l+[i]
        if (n[i]=="(" ):
              p=p+1
              m=m+[i]
             
    if (p==q and l>=m):
         return(True)
    else:
         return(False)
                         

    
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))
              