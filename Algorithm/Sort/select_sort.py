# 選択ソート
data = [9, 3, 7, 1, 4, 2, 5, 8, 6, 0]
print(data, "元のデータ")

for i in range(0, 9):
    m = i # 最小値のインデックスを保持する変数
    for j in range(i+1, 10):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i] # 入れ替え
    print(data,i+1) # プロセスの出力

print(data, "ソート後のデータ")
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ソート後のデータ