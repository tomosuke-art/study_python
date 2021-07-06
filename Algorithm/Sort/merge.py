# マージソート
a = [1,3,4,7,8,9]
b = [0,2,5,6]
na = len(a)
nb = len(b)
c = [0]*(na+nb) # 要素数na+nbの配列
i = 0
j = 0
p = 0

print(a,'データA')
print(b,'データB')

while i < na and j < nb: # 要素分繰り返す
    # aとbを比べ、小さい方をcに入れる
    if a[i] <= b[j]:
        c[p] = a[i]
        i += 1
        p += 1
    else:
        c[p] = b[j]
        j += 1
        p += 1
while i < na: # データAの残りをcにいれる
    c[p] = a[i]
    i += 1
    p += 1
while j < nb: # データBの残りをcに入れる
    c[p] = b[j]
    j += 1
    p += 1
print(c,'マージ後のデータ')