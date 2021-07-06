# 文字列探索
# 力任せ法
text  ="I`m learning Python.It`s interesting!" 
pattern = 'Python' # 探索するパターン(単語)
tn = len(text)
pn = len(pattern)
flg = False
p = 0

while p <= tn-pn:
    c = 0
    for i in range(pn):
        if text[p+i] != pattern[i]:
            break
        c += 1
    if c == pn: # パターンが見つかった
        flg = True
        break
    p += 1

print(text)
if flg == True:
    print(str(p+1) + '文字目に' + pattern + 'があります')
else:
    print(pattern + 'は見つかりませんでした。')