# ユークリッドの互除法

# 自作ver
def euclid(a,b):
    while True:
        if a % b == 0:
            print("最大公約数は",b)
            break
        else:
            c = a % b
            a = b
            b = c
a = int(input("a="))
b = int(input("b="))
euclid(a,b)

# 書籍ver
print('a>=bとなる自然数を入力してください')
a = int(input("a="))
b = int(input("b="))
while True:
    r = a%b
    if r == 0:
        print('それらの数の最大公約数は',b)
        break
    a = b
    b = r

# 再起関数を用いる場合
def euclid2(x,y):
    if y == 0:
        return x
    else:
        return euclid2(y,x%y)
print('x>=yとなる自然数を入力してください')
x = int(input("x="))
y = int(input("y="))
print('最大公約数は',euclid2(x,y))