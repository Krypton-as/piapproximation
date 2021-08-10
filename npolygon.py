import math

def sin(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return math.sqrt((1-(math.sqrt(1-(sin(n-1))**2)))/2)

for i in range(1,40):
    f=2**(i-1)
    g=sin(i)
    h=f*g
    print(h)
