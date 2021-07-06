# 練習問題

# pra①
a = [10,-5,0,29,6,2,77,8]
for i in a:
    if i % 2 == 0:
        print(str(i)+"は偶数です")
    else:
        print(str(i)+"は奇数です")

# pra②
def three(n):
    return 3 ** n
def two(m):
    return 2 ** m
for j in range(1,6):
    print(three(j) - two(j))

# pra② 別解
for x in range(1,6):
    v1 = 3**x
    v2 = 2**x
    print("3の{}乗と2の{}乗の差は{}".format(x,x,v1-v2))