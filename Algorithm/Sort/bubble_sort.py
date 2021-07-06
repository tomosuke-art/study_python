# バブルソート
data = [9,4,7,2,3,8,6,1,5,0]
n = len(data)
print(data,'元のデータ')

for i in range(0,n-1):
    for j in range(n-1,i,-1):
        if data[j-1] > data[j]: # 左の値の方が大きいなら
            data[j],data[j-1] = data[j-1],data[j] # 左右入れ替え
print(data,'ソート後のデータ')