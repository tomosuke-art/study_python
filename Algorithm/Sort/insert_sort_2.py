# 挿入ソート
# 並び替えるデータを乱数で
import random
n = 15 # データ個数
data = [0]*n
for i in range(n):
    data[i] = random.randint(1,99)
print(data,'元のデータ')

for i in range(1,n):
    tmp = data[i]
    j = i
    while j>0 and data[j-1]>tmp: # tmpより大きな値を右にずらす
        data[j] = data[j-1]
        j = j - 1
    data[j] = tmp # ずらした先頭にtmpの値を挿入
print(data,'ソート後のデータ')