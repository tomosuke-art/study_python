"""
あなたは、500円玉を A枚、100円玉を B枚、50円玉を C枚持っています。
これらの硬貨の中から何枚かを選び、合計金額をちょうど X円にする方法は何通りありますか。
同じ種類の硬貨どうしは区別できません。
2通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。

制約
・0 ≤ A, B, C ≤ 50
・A + B + C ≥ 1
・50 ≤ X ≤ 20000
・A, B, C は整数である
・X は 50 の倍数である
入力
入力は以下の形式で標準入力から与えられる。
A
B
C
X

解法
500 円玉が 0 枚 〜 A 枚の場合 (A + 1 通り)
100 円玉が 0 枚 〜 B 枚の場合 (B + 1 通り)
50 円玉が 0 枚 〜 C 枚の場合 (C + 1 通り)
をすべて探索します。全部で、(A + 1)(B + 1)(C + 1) 通りの場合があります。

"""
a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if i*500 + j*100 + k*50 == x:
                count += 1
print(count)

# 別解
a,b,c,x=map(int,open(0))
print(
  sum(
    [500*i+100*j+50*k==x
       for i in range(a+1)
       for j in range(b+1)
       for k in range(c+1)]
   )
)

N,A,B = map(int,input().split())
count = 0
x = []
for i in range(1,N + 1):
  if A <= i and i <= B:
    count += i
  a = len(str(i))
  if a == 2:
    while i > 0:
      x.append(i % 10)
      i //= 10
    x.reverse()
    y = int(x[0]) + int(x[1])
    if A <= y and y <= B:
      count += y
print(count)