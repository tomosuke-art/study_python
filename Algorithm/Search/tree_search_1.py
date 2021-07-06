# 木探索
LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1,   2,   10],
    [3,   4,    5],
    [5,   None,12],
    [None,None, 2],
    [6,   7,    8],
    [None,None,11],
    [None,None, 6],
    [None,None, 9],
]

def traverse(p): # 気を巡回する再起関数の定義
    if p != None:
        traverse(node[p][LEFT])
        print(node[p][DATA])
        traverse(node[p][RIGHT])
print('二分木探索を通りがけ順に巡回')
traverse(0)