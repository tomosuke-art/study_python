# 暗号学的ハッシュ関数
import hashlib
print('SHA-256のハッシュを生成します')
print('何も入力しないと終了します')
while True:
    s = input('文字列を入力してください')
    if s == "":
        break
    h = hashlib.sha256(s.encode()).hexdigest()
    print(h)