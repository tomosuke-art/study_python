"""
問題文
1以上 N以下の整数のうち、10進法での各桁の和が A以上 B以下であるものの総和を求めてください。

制約
1≤N≤10**4
1≤A≤B≤36
入力はすべて整数である

入力
入力は以下の形式で標準入力から与えられる。
N A B

入力例
20 2 5
84

20以下の整数のうち、各桁の和が 2以上 5以下なのは 2,3,4,5,11,12,13,14,20です。
これらの合計である 84を出力します。
"""

n,a,b = map(int,input().split())
count1 = 0
count2 = 0
for i in range(1,n+1):
  if a <= i and i <= b:
    count1 += i
  if i > 10:
    # 数値を文字列に変換
    s = str(i)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
  
    x = sum(array) # リスト内の数値の合計
    if a <= x and x <= b:
      # print(x)
      count2 += i
count3 = count1 + count2
print(count3)

# 解答
n, a, b = map(int, input().split())
ans = 0
for i in range(n + 1):
  if a <= sum([int(x) for x in str(i)]) <= b: # ※[int(x) for x in str(’13’)] を動かすと、[1, 3] というリストができます。
    ans += i
print(ans)

# 解答2
N, A, B = map(int, input().split())
ans = 0


# 各桁の和を計算する関数
def Digits(x):
    count = 0
    while x > 0:
        count += x % 10
        x = x // 10
    return count


for n in range(1, N + 1):
    count = Digits(n)
    if A <= count <= B:
        ans += n


print(ans)

