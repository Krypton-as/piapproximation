import numpy as np
def fourier(n):
    return 1/(n**2)

for i in range(1,10000,100):
    h=0
    for j in range(1,i):
        k=fourier(j)
        h+=k
    l=np.sqrt(6*h)
    print(l)    
        
