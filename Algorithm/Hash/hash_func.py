# ハッシュ関数の実装
def hash(key):
    h = 0
    for i in key:
        if i != " ": # その文字が半角スペースでなければ -> [プログラム]と[プロ グラム]が同じハッシュ値
            h += ord(i) # hに文字のユニコードを加える
    return(h%1000)

print('文字列をハッシュ値に変換します')
print('何も入力しないと終了します')
while True:
    s = input('文字列を入力してください')
    if s == "": # 何も入力しなければ処理を終了
        break
    print(s,"->ハッシュ値",hash(s))