def wal(n):
    return (4*(n**2))/(4*(n**2)-1)
f=1
for i in range(1,10000):
    if i % 100==0:
        f*=wal(i)
        g=2*f
        print(g)
    else:
        f*=wal(i)
