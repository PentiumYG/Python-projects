# -*- coding: utf-8 -*-
""" Program to calculate gems in a Jar """
#from statistics import mean
from scipy import stats



Estimate = [12,3,21,32,43,43,54,54,43,43,21,21,34,45,54,43,545,567,5434,54,66,45,6456,54,56,4,654,645,45,67,65,67,78,87,54,23,54,34,65,76,4,54,3,54,6,56,76,4,67,3]
Estimate.sort()
#tv = int(0.1 * len(Estimate))
#Estimate = Estimate[tv:len(Estimate)-tv]
#print(mean(Estimate))

m = stats.trim_mean(Estimate, 0.1)
print (m)
