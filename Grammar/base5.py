# 高階関数
# 関数を変数のように扱う(引数や返り値として使う)
def print_hello():
    print('hello')
def print_goodbye():
    print('goodbye')
var = ['AA','BB',print_hello,print_goodbye]
# 変数化しない書き方
var[2]() # hello
var[3]() # goodbye

def prtint_world(msg): # msg = hello
    print('{} world'.format(msg))
def print_konnichiwa():
    print('こんにちは')
def print_hello(func):
    func('hello') # func = print_world
    return print_konnichiwa
var = print_hello(prtint_world)
var()

# lambda式
# 1行で関数を定義する
# lambda 引数:返り値

# if文を1行で
y = 10
x = 0 if y > 0 else 1 # y>0 => 0, else => 1
print(x) # 0

lambda_a = lambda x: x*x # 引数x:返り値x*x
print(lambda_a(10)) # 100
lambda_b = lambda x,y,z=5: x*y*z # デフォルト値は書き換え可能
print(lambda_b(2,3)) # x=2,y=3,z=5 => 30

# 条件つきlambda
lambda_c = lambda x,y: y if x < y else x # if(x<y)=> y, else x
print(lambda_c(2,4))

# 再帰(実務ではほぼ使わない->プログラムが無限ループする可能性があるため)
def sample(a):
    if a < 0:
        return
    else:
        print(a)
        sample(a-1)
sample(10) # 10,9,8,7,6,5,4,3,2,1,0

# フィボナッチ数列
def fib(n):
    return 1 if n < 3 else fib(n-1) + fib(n-2)
for x in range(1,10):
    print(fib(x))

# リスト内包表記
# 1行でリストを作成する方法
list_a = (1,2,3,4,'a','b',6) # タプル
new_list = []
for x in list_a:
    new_list.append(x)
# 上記処理を1行で
new_list = [x for x in list_a if type(x) == int] # int型のみ格納
print(new_list)

dict_a = {
    'a':'Apple',
    'b':'Banana'
}
list_c = [dict_a.get(x) for x in list_a if type(x) == str] # list_aから'a','b'のみ取り出す
print(list_c)

list_a = {x for x in range(100)}
print(list_a)

# デコレータ関数
# 関数そのものを変更できる
def my_decorator(func):
    def wrapper(*args,**kwargs):
        
        print('*' * 100)
        func(*args,**kwargs)
        print('*' * 100)
    return wrapper
# 同じ処理を共通で持てる
@my_decorator
def func_a(*args,**kwargs):
    print('func_aを実行')
    print(args)

@my_decorator
def func_b(*args,**kwargs):
    print('func_bを実行')
    print(args)

func_a(1,2,3)
func_b(1,2,3)

# Map関数
# リストの全ての要素にアクセスできる
list_a = [1,2,3,4,5]
map_a = map(lambda x: x * 2, list_a)
for x in map_a:
    print(x) # 2,4,6,8,10

man = {
    'name':'Mikasa',
    'age': '18',
    'country':'Eludia'
}

map_man = map(lambda x:x + ',' + man.get(x),man)
for x in map_man:
    print(x)

def calcurate(x,y,z):
    if z == 'plus':
        return x + y
    elif z == 'minus':
        return x - y
map_sample = map(calcurate, range(5),[3,3,3,3,3],['plus','minus','plus','minus','plus'])
for x in map_sample:
    print(x)