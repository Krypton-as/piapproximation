import numpy as np
def update(a,b,t,p):
    new_a=(a+b)/2
    new_b=np.sqrt(a*b)
    new_t=t-p*(a-new_a)**2
    new_p=2*p
    return new_a,new_b,new_t,new_p
a=1.0
b=1/np.sqrt(2)
t=0.25
p=1.0
for i in range(1,100):
    a,b,t,p=update(a,b,t,p)
    h=(a+b)**2/(4*t)
    print(h)
