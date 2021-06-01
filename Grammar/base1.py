# format関数(変数の埋め込み)
name = "エレン・イェーガー"
age = 15
print('俺の名前は = {},年齢は {}'.format(name,age))
print(f'名前 = {name}') # 3.6
print(f'{name=}') # 3.8
# 定数 =  変更してはいけない変数(pythonは機能上できないが全て大文字で定義するようにする)
ANIMAL = "Lion"

# 論理型 True False
is_animal = True
if is_animal:
    print("動物です")

is_man = True
is_adult = True
# or文(どっちか)
if is_man or is_adult:
    print("男か大人です")
# and文(どっちも)
if is_man and is_adult:
    print("成人男性です")

# データ構造
# 数値型 int,floatの2つのみ
value = 10
print(10 // 3) #切り下げられて 3 になる

# シフト演算
shift = 8
print(shift >> 2) # 1000 -> 0010(2)
print(shift << 3) # 1000 -> 1000000(64)

# ビット演算
print(12 & 21) # 01100 and 00100 = 00100 -> 4
print(12 | 21) # 01100 or 10101 = 11101 -> 29

# 複素数(業務ではほぼ使わない)
# ex.実数3,虚数2の場合、3+2jと表示
a = 1 + 3j
b = 3 + 5j
print(a,b)
print(a+b)
print(a-b) # -2-2j
print(a*b) # -12+14j

# Complex関数を使う
a = complex(1,3)
b = complex(3,5)
print(a,b)
print(a.real) # 実数
print(a.imag) # 虚数

# 文字列型
fruit = "apple"
print(fruit * 10) # 文字列*数値の掛け算できる

# encode,decode -> bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit) # b'apple
print(type(byte_fruit))
# 元に戻す
str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)

# startwith, endwith
msg="ABCDEABC"
print(msg.startswith("ABC")) # True(ABCで始まってるか)
print(msg.endswith("D")) # False

# 文字列の一部取り出し
msg = "hello, my name is taro"
print(msg[:6]) # hello
print(msg[6:]) #  my name is taro



