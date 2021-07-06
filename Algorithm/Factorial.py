# 10!
num = [10,9,8,7,6,5,4,3,2,1]
answer = 1
for i in num:
    answer *= i
print("10!=",answer)

# 別解(関数使用)
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(10))
for j in range(10,21): # 10! ~ 20!
    print(str(j) + "! =",fact(j))