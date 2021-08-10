import math
def ram(n):
    return ((((-1)**n)*math.factorial(4*n))*(1123+21460*n))/((882**(2*n+1))*((4**n)*math.factorial(n))**4)
t=0
for i in range(0,10000,100):
    s=ram(i)
    t+=s
    u=4*(1/t)
    print(u)
