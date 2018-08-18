# -*- coding: utf-8 -*-
#print("Please specify the value of n:")
#n = input()
#print("The value of n is : ",n)

for i in range(1,101):
    if(i==0):
        print("Value of i is 0")
    if(i % 3 == 0):
        print(i," fizz")
    if(i % 5 == 0):
        print(i," buzz")
    if(i % 3 == 0 and i % 5 == 0):
        print(i," fizz-buzz")
        