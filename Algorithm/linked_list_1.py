# 線形リスト
MAX = 5
data = [None]*MAX # データを代入する配列(全てにNone)
pointer = [None]*MAX
head = 0 # 先頭ノードの位置を管理

def add_list(d):
    n = -1 # データが入れる空きが無い状態
    for i in range(MAX):
        if data[i] == None: # 空いている配列があれば
            n = i 
            break # 繰り返し抜ける
    if n == -1:
        print('データ領域に空きがありません')
        return False
    for i in range(MAX):
        if data[i] != None and pointer[i] == None: # 最後尾のノードを探す
            pointer[i] = n # 追加するノードを指すポインタの値を代入
            break
    data[n] = d # データを格納
    pointer[n] = None # そのポインタをNoneとする(末尾)
    print('データ',d,'を追加しました')
    return True

def del_list(d):
    global head
    n = -1
    for i in range(MAX):
        if data[i] == d: # 引数の値が存在していたら
            n = i 
            break
    if n == -1:
        print('そのデータは存在しません')
        return False
    if n != head:
        for i in range(MAX):
            if pointer[i] == n: # ノードを指すポインタを探す
                pointer[i] == pointer[n] # ポインタの付け替え
    else:
        head = pointer[n]
        if head == None:
            head = 0 # 配列の先頭にする
    data[n] = None # データ削除
    pointer[n] = None # ポインタ削除
    print('データ',d,'を削除しました')
    return True
    
def put_list(): # リストのデータ一覧を出力する関数
    p = head
    while True: # 無限ループで繰り返す
        print(data[p],end="->")
        if pointer[p] == None: # pointer[p]が末尾になったら
            print('EOF')
            break
        p = pointer[p] # 次のノードにする

for i in range(10,70,10):
    add_list(i)
del_list(10)
put_list()