# 例外処理
try:
    b = [10,20,30]
    a = b[4]
    a =  10 /0
except ZeroDivisionError as e:
    import traceback
    # エラー内容の詳細表示
    traceback.print_exc()
    # エラー内容表示
    print(e)
    pass
except IndexError as e:
    print("インデックスエラー発生")
except Exception as e: # 全てのエラーをキャッチ
    print('Exception: ',e,type(e))
# 例外が発生した場合は実行されない
# tryと処理を分けるときに使う
else: 
    print("else処理")
# 例外が発生してもしなくても実行
finally:
    print("処理が完全に終了")

print("処理が完了しました")

# raise 例外自作
class MyException(Exception):
    pass

def devide(a,b):
    if b == 0:
        # 例外を返す
        # raise ZeroDivisionError('0で割り切れません')

        # 例外自作
        raise MyException('0では割り切れません')
    else:
        return a/b
try:
    c = devide(10,0)
except Exception as e:
    print(e,type(e))

# 関数
# デフォルト値の指定
def sample(arg1, arg2 = 100):
    print(arg1,arg2)
sample(200) # 第二引数はデフォルト値

# 可変長引数(宣言は一つのみ)
# *arg = タプルとして表示
def spam(arg1,*arg2):
    print("arg = {}, arg2 = {}".format(arg1,arg2))
    print(type(arg2))
spam(1,2,3,4,5)
# 出力
#arg = 1, arg2 = (2, 3, 4, 5)

# **arg = 辞書式で表示
def spam2(arg1,**arg2):
    print("arg = {}, arg2 = {}".format(arg1,arg2))
    print(type(arg2))
spam2(3,name="eren",age=15)
# 出力
# arg = 3, arg2 = {'name': 'eren', 'age': 15}

# 複数の返り値
def sample2():
    return 1,2,3
a,b,c = sample2()
print(a,b,c)

# グローバル変数
# 名前空間 = 利用できる領域
# 関数内の変数を関数外でも利用できる
def printAnimal():
    global animal
    animal = "Cat"
    print('関数内animal = {},id = {}'.format(animal, id(animal)))
animal = "Dog"
printAnimal()
print("関数外animal = {},id = {}".format(animal, id(animal)))

# inner関数(外→内),ノンローカル変数
def outer():
    outer_value = "外側の変数"
    def inner():
        # ノンローカル変数を使うと外側の変数も書き変わる
        nonlocal outer_value
        outer_value = '内側の変数'
        print('inner:outer_value = {}, id = {}'.format(outer_value,id(outer_value)))
        # print('A')
    inner()
    print('outer:outer_value ={}, id = {}'.format(outer_value,id(outer_value)))
outer()

# ジェネレーター関数

def generator(max):
    print("ジェネレータ作成")
    for n in range(max):
        try:
            x = yield n # send()
            print('x = {}'.format(x))
            print("yeild実行")
        except ValueError as e:
            print("throwを失効しました")
gen = generator(10)
# 実行①
n = next(gen) 
print('n = {}'.format(n))
# 実行②(ループ分で実行)
# for x in gen:
#     print('X = {}'.format(x))

# send() 値を送出
next(gen) # x = None
gen.send(100)
# 例外を発生させる
gen.throw(ValueError('Invalid Error'))

# ジェネレータ関数の使い道 → メモリ使用量を削減する
# DBから大量のデータを引っ張ってくるとき

# 使用量の比較
import sys
list_a = [i for i in range(100000)]
def num(max):
    i = 0
    while i < max:
        yield i
        i += 1
gen = num(100000)
print(sys.getsizeof(list_a)) # 800984
print(sys.getsizeof(gen)) # 112

# サブジェネレータ関数
# ジェネレータからジェネレータを呼び出せる
# 呼び出し先->サブジェネレータ

def sub_sub_generator():
    yield "sub subのyeild"
    return "sub sub のreturn" # return->呼び出し元(sub_generator)に値を返す
def sub_generator():
    yield "subのyield"
    res = yield from sub_sub_generator() # サブジェネレーターの呼び出し->returnの値を格納
    print("sub res ={}".format(res))
    return "subのreturn"

def generator():
    yield "generatorのyeild" # yield -> 処理を停止してメインに値を返す
    res = yield from sub_generator()
    print('gen res = {}'.format(res))
    return 'generatorのreturn'

gen = generator()
print(next(gen)) # generatorのyeild
print(next(gen)) # subのyield
print(next(gen)) # sub subのyeild
print(next(gen)) # sub res =sub sub のreturn
print(next(gen)) # gen res = subのreturn
