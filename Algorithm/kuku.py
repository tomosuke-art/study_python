for i in range(1,10):
    for j in range(1,10):
        print(i,'x',j,'=',i*j)

# 別解
for x in range(1,10):
    k = ""
    for y in range(1,10):
        k = k + "{}x{}={:2d} ".format(y,x,x*y)
    print(k)