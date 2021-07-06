# 線形探索
data = [57,48,46,52,45,59,61,60,49,71]
n = len(data)
key = 60 # 目的の値
flag = False
for i in range(n):
    if data[i] == key:
        print('data[{}]が{}です'.format(i,key))
        flag = True
        break
if flag == False:
    print(str(key)+'は存在しません')