# 線形探索 その２
data = [57,48,46,52,45,59,61,60,49,71]
n = len(data)
key = 60 # 目的の値
i = 0
while i < n and data[i] != key:
    i += 1
if i == n: # iの値がデータの終わりに達したら
    print(str(key) + "存在しません")
else:
    print('data[{}]が{}です'.format(i,key))