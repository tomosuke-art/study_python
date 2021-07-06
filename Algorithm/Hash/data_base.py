# ハッシュテーブル
# ハッシュの衝突
# 同じハッシュは上書きされる
HASH = 5
name = [None]*HASH
tel = [None]*HASH

def hash(key):
    h = 0
    for i in key:
        h += ord(i) # 文字を一つづつユニコード化して足し合わせる
    return h%HASH # 最後に5で割る

while True:
    n = input("名前を入力してください")
    if n =="":
        break
    t = input("番号を入力してください")
    h = hash(n) # ハッシュを生成しhに格納
    name[h] = n
    tel[h] = t
    print('ハッシュ値',h,'データ格納完了')

print(name)
print(tel)

while True:
    n = input('検索する名前は？ ')
    if n == '':
        break
    h = hash(n)
    if name[h] == n:
        print(n+'さんの番号は'+tel[h])
    else:
        print('その名前は登録されてません')
