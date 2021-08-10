
for x in range(0,10000,100):
    t=x+1
    sig=0
    for i in range(t):
        count=((-1)**i)/((2*i)+1)
        sig+=count
    h=4*sig
    print(h)


