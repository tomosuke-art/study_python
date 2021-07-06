# 二分木
LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1,2,10], # [LEFT,RIGHT,DATA]
    [3,4,20],
    [5,None,30],
    [None,None,40],
    [6,7,50],
    [None,None,60],
    [None,None,70],
    [None,None,80],
]
MAX = len(node)

print('指定の番号のノードを調べます')
print('何も入力せずにEnterを押すと終了します')

while True:
    s = input('number=') # nodeのindex
    if s == "":
        break
    try:
        n = int(s)
    except:
        print('数値を入力してください')
        continue    # while文の初めに戻す -> エラーが出ても処理は止まらない
    if 0 <= n and n < MAX: # 入力値が0~7の数字だったら
        print('node{}の値は{}'.format(n,node[n][DATA])) 
        le = node[n][LEFT]
        if le != None:
            print('左の子は' + str(node[le][DATA]))
        else:
            print('左の子は存在しません')
        ri = node[n][RIGHT]
        if ri != None:
            print('右の子は' + str(node[ri][DATA]))
        else:
            print('右の子は存在しません')
    else:
        print('0から' + str(MAX-1) + 'の範囲で入力してください')