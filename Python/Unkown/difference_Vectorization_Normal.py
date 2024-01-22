import numpy as np,pandas as pd
import time
x,w,n =[],[],500000
x = np.random.randint(1, 200, n)
w = np.random.randint(1,200,n)
b = 10
start_time = time.time()
#==================
f = 0
for j in range(n):
    f += (w[j]*x[j])
f+=b
print(f)
#=================
timing1 = -1*start_time+time.time()
#===================
starttime2 = time.time()
ff = np.dot(w,x)+b
print(ff)

timeing2 = time.time()-starttime2

print(timing1)
print(timeing2)