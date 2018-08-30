# -*- coding: utf-8 -*-



def matrixFunc():
    r,c = input().split()
    r = int(r)
    c = int(c)
    count = 1
    matrix =[]
    for i in range(1,r+1):
        l = []
        for j in range(1,c+1):
            l.append(count)
            count = count + 1
        matrix.append(l)
        
            
        
    for i in range(r):
        for j in range(c):
            if(j<(c-1)):
                print(matrix[i][j], end=" ")
            else:
                print(matrix[i][j])
        


matrixFunc()