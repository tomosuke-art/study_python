# 最短経路の経路を記憶する
F = 99999  # 十分に大きな値 (無限大)
way = [
    [F,3,2,5,F,F,F],
    [3,F,F,F,7,F,F],
    [2,F,F,2,F,4,F],
    [5,F,2,F,F,1,F],
    [F,7,F,F,F,4,5],
    [F,F,4,1,4,F,3],
    [F,F,F,F,5,3,F],
]

dist = [F]*7 # 最短距離を代入する配列
flg = [0]*7 # フラグ用の配列
route = [-1]*7 # 経路を保持する配列
start = 0
p = start # pの値を変化させながら、最短距離を求める
dist[p] = 0
print('始点',p)

for i in range(7):
    d = F
    for j in range(7):
        if flg[j] == 0 and dist[j] < d:
            p = j
            d = dist[j]
    flg[p] = 1
    for k in range(7):
        if dist[p]+way[p][k] < dist[k]:
            dist[k] = dist[p] + way[p][k]
            route[k] = p

print('各ノードまでの最短距離')
for i in range(7):
    print('ノード{}まで{} '.format(i,dist[i]))
print('routeの値',route)
e = int(input('道順を示すノード番号は？'))
while route[e] >= 0:
    print(e,end="<-")
    e = route[e]
print(start)