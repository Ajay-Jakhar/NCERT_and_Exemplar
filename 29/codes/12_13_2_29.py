#Code by G V V Sharma
#October 13, 2023

#Generating binomial r.v.
#Release under GNU/GPL

import numpy as np

from scipy.stats import bernoulli

p1 = 1/10
p2 = 2/5
X1 = bernoulli.rvs(p1, size=1000)
X2 = bernoulli.rvs(p2, size=1000)
X = X1+X2
count0=0
count1=0
count2=0
for i in range(1000):
    if X[i] == 0:
        count0 = count0+1
    if X[i] == 1:
        count1 = count1+1
    if X[i] == 2:
        count2 = count2+1

print(count0/1000,27/50,count1/1000,21/50,count2/1000,2/50)
#print(X[i])
#print(X1, '\n', X2)
#print(X)
