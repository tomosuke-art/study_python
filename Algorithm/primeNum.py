# 素数判定
flag = 0
for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
            print(i)
# 別解
for x in range(2,101):
    h = x // 2
    f = True
    for y in range(2,h+1): 
        if x % y == 0:
            f = False
            break
    if f == True:
        print(x,end=",")

# エラトステネスの篩
p = [True]*100 # 要素数100の配列の要素にTrueを代入
p[0] = False
p[1] = False
n = 2

def hyou(): # 数の一覧を表示する関数
    s = ""
    for i in range(100):
        if p[i] == True:
            s += "{:2d}, ".format(i)
        else:
            s += "/, "
        if i % 10 == 9: # 数字10個ごとに改行
            s += "\n"
    print(s)
        
def furui(): # 篩い落とす関数
    global n
    for i in range(n+n,100,n): # iはn+nから99までnづつ増える
        p[i] = False # nの倍数を篩い落とす
    print(n,"の倍数を篩い落としました")
    hyou()
    while n < 100: # 次に篩い落とす数
        n += 1
        if p[n] == True:
            break
hyou()
while n<10: # nが10未満の間実行
    input("Enterキーを押してください")
    furui() # 篩い落とすアルゴリズム実行