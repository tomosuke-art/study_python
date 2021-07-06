# 二分木探索
data = [1,2,9,12,20,25,32,48,50,59,72,78,80,93,94,95,99,100]
key = int(input("探す値を入力してください"))
left = 0
right = len(data)-1
flg = False # 目的の値を見つけたらTrueに

while left <= right:
    mid = (left+right) // 2
    print('L={} M={} R={}'.format(left,mid,right))
    if data[mid] == key:# 目的の値が見つかったら
        print('data[{}]が{}です'.format(mid,key))
        flg = True
        break
    if data[mid] < key: 
        left = mid + 1
    else:
        right = mid -1
if flg == False:
    print('その値は見つかりませんでした')
