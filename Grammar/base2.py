# リスト操作
# copy
list_a = [1,2,3,4,5]
list_b = list_a.copy() # list_aは上書きされない
list_b[0] = "AAAAA"
print(list_a)
print(list_b)

# 辞書型
# dectionary = {'key1':"value1",'key2':"value2"}
car = {'brand':'Toyota','Model':'Prius','Year':2015}
print(car['brand']) # Toyota
print(car.get('brand')) # Toyota
# keyとvalueの一覧
for k,v in car.items():
    print('key = {}, value = {}'.format(k,v))
if 'brand' in car:
    print('carのブランドは{}'.format(car['brand']))


# 追加/更新
tmp_car =  {'country':'Japan','prefecture':'Aichi','model':'カローラ'}
car.update(tmp_car)
print(car)
# 最終要素の取り出し
value = car.popitem()
print(value)

# タプル
# 値を変更・追加できないリスト
# リストよりアクセスするスピードが速い
fruit = ("apple","banana","orange","lemon")
#fruit[0] = "grape" # 変更できない、エラーになる
fruit = fruit + ("grape",) # 追加はできる
print(fruit)

list_fruit = ["apple","banana"]
# リストをタプルに変換
fruit = tuple(list_fruit)
print(fruit)

pos = (135,35)

countries = {pos: "Japan"}
# タプルに対応した値を返す
print(countries.get((135,35)))

# セット(set)
# 同じ値を持たない(重複なし)

set_a = {'a','b','c','d','a',12}
print(set_a) # 'a'は一つだけ出力
print('e' in set_a) # False
print('a' not in set_a) # False

set_a.add('A') # 追加
set_a.remove('A') # 要素の削除
#set_a.descard(12) # 要素の削除(存在しない要素でもエラーにならない)
set_a.pop() # 任意の要素の取り出し
set_a.clear() # 全クリア

# セットメソッド
s =  {"a","b","c","d"}
t = {"c","d","e","f"}
# 和集合 (どちかにか含まれる要素)
u = s | t
u = s.union(t)
print(u)
# 積集合(共通する要素)
v = s & t 
v = s.intersection(t)
print(v)
# 差集合
w =  s - t # sにのみ含まれる要素
w = s.difference(t)
print(w)
# 対象差(積集合の反対)
r =  s ^ t 
r = s.symmetric_difference(t)
print(r)

# issubset
s = {"apple","banana"}
t = {"apple","banana","lemon"}
u = {"cherry"}

print(s.issubset(t)) # True(一部含んでいるか)
print(s.issuperset(t)) # False(全て含んでいるか)
 # 重複要素はないか
print(t.isdisjoint(s)) # False(重なっている要素が一つでもないか)
print(t.isdisjoint(u)) # True

## if文
class ClassA():
    def __init__(self, a):
        self.a = a
    
    def __bool__(self):
        if self.a == 'a':
            return True
        return False
        
var = ClassA('a') # 'b'だとFalse
print('boolの計算結果: {}'.format(bool(var)))
if var:
    print("if分の処理")

# all,any関数
# allはオブジェクトの中の全てがTrueの場合実行
# リストやタプルをつける
if all((True,True,True,10 < 20,"a" == "a")):
    print("allの処理")
# anyは一つでもTureがあれば実行
if any((False,True,10 >> 100,"a" == "c")):
    print("anyの処理")

## ループ文(for,while)
for _ in range(100):
    # print("A")
    pass
for i in range(2,20,3):
    print(i) # 2から20まで3つ飛ばしで表示
 # 辞書型の取り出し
Shingeki = {
    "Eren":"man",
    "Mikasa":"woman",
    "Arumin":"man" 
}
for h in Shingeki:
    # keyとvalue両方の表示
    print(h,Shingeki.get(h))

 #eumerate関数(配列の値とインデックスを同時に取得)
manga = ["進撃の巨人","怪獣８号","ヒロアカ","NARUTO"]

for index, value in enumerate(manga):
    print('index = {}'.format(index))
    print('タイトル = {}'.format(value))
 #zip関数(2つの配列の値を同時に取得)
classA = ["HIsayama","Horikosi","Toriyama"]
classB = ["Inoue","Ochiai","Oda"]
for A ,B in zip(classA,classB):
    print('classA student: {}'.format(A))
    print('classB student: {}'.format(B))
# 0~9まで
count = 0
while count < 10:
    print(count)
    count += 1

# countinue,break,else
for i in range(10):
    if i == 3:
        continue # 3の時のみスキップ
        # break # 3の時ループの外に出る
    print(i)
else:
    print("処理終了")

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print("処理終了")
## セイウチ演算子
# 変数の代入と使用を同時に実行
if (num := 10) > 5:
    print('5より大きい:{}'.format(num))
n = 0
while(n := n + 1)<10:
    print(n)

# 演習 FizzBuzz
for i in range(1,101):
    if i % 15 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)