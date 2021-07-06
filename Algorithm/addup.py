# 1 ~ 10 までの足し算
score = 0
for i in range(1,11):
    score += i
print(score) 

# 1 ~ n までの足し算
def add(max):
    a = 0
    for i in range(max + 1):
        a += i
    return a
print(add(10))

# 別解(計算量が少なく効率がいい)
# (初めの数 + 終わりの数)*(足し合わせる個数/2)
def addup_other(n):
    a = (1+n)*n/2 
    return int(a) # 小数を整数に変換
print(addup_other(10))