# スタック
# 最後に入れたデータを最初に取り出す仕組み
MAX = 5 # スタックデータの総数
stack = [0]*MAX
sp = 0 # スタックポイント(データを出し入れする位置を管理)

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp += 1
        print('データ',d,'を追加しました')
    else:
        print('これ以上データは入れられません')

def pop():
    global sp
    if sp > 0:
        sp -= 1
        return stack[sp]
    else:
        print('取り出すデータが存在しません')
        return None
for i in range(6):
    push(i)
for i in range(6):
    d = pop()
    print('取り出したデータ',d)