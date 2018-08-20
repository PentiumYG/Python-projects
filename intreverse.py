# -*- coding: utf-8 -*-

def intreverse(n):
    startmsg = str(n)
    endmsg = ""
    for i in range(0,len(startmsg)):
        endmsg = startmsg[i] + endmsg
    endmsg=int(endmsg)
    return(endmsg)

n=input()
print(intreverse(n))
      