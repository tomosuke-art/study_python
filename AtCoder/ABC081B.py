"""
黒板に N個の正の整数 A1,...,ANが書かれています．
すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．
黒板に書かれている整数すべてを，2で割ったものに置き換える．
すぬけ君は最大で何回操作を行うことができるかを求めてください．
"""
n = int(input())
S = list(map(int,input().split()))
count = 0
# newS = []
while all(x % 2 == 0 for x in S): # すべての要素が当てはまるとTrue
  S = [i / 2 for i in S] # リスト内包表記
  count += 1
print(count)
# print(S)

# 別解
n = int(input())
S =  list(map(int, input().split()))
count = 0

# 別解
n = int(input())
S = list(map(int, input().split()))
ans = 0
while True:
  if [i for i in S if i % 2 == 1]:
    break
  S = [i/2 for i in S]
  ans += 1
print(ans)