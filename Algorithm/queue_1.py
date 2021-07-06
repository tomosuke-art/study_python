# キュー
# 最初に入れたデータを最初に取り出す仕組み(待ち行列とも言う)
# リングバッファを用いて、キューのデータ構造を実装  
MAX = 6 # データの総数の+1を定義
que = [0]*MAX # 全ての要素が0の配列
head = 0   # 取り出す位置
tail = 0   # 入れる位置

def enqueue(d): # データを入れる処理
    global tail
    nt = (tail + 1)%MAX # データを入れた時の次の位置をntに代入
    if nt == head:   # i=5の時,6 % 6 = 0 となる(nt == head)
        print('これ以上データを入れられません')
    else:
        que[tail] = d
        tail = nt
        print('データ',d,'を追加しました')

def dequeue():
    global head
    if head == tail:
        print('取り出すデータが存在しません')
        return None
    else:
        d = que[head]
        head = (head+1)%MAX
        return d

for i in range(6):
    enqueue(i)
for i in range(6):
    d = dequeue()
    print('取り出したデータ',d)