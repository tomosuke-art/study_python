# クラスの定義
class Car:
    """車クラス""" # ドキュメンテーション文字列
    countory = "Japan"
    year = 2019
    name = "Prius" # プロパティ
    def print_name(self):
        print("print_name実行")
        print(self.name)
my_car = Car() # インスタンス化
print(my_car.year)
my_car.print_name()
# リストの中にもクラスを入れられる
list_a = ["a","b",Car]
second_car = list_a[2]()
second_car.print_name()
# help(Car) # ドキュメンテーション文字列を表示

# インスタンス変数,クラス変数
class SampleA():
    class_val = 'class val' # クラス変数
    def set_val(self):
        self.instance_val = 'instance val' # インスタンス変数 
    
    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val))
        print('インスタンス変数 = {}'.format(self.instance_val))

instance_a = SampleA() #インスタンス化
instance_a.set_val() # インスタンス変数の設定
print(instance_a.instance_val) # インスタンス変数の表示
instance_a.print_val()
print(SampleA.class_val)
print(instance_a.__class__.class_val) # クラス変数(class val)

instance_b = SampleA() #インスタンス化
instance_b.set_val()
instance_b.print_val()
instance_a.__class__.class_val = 'class val 2' # クラス変数はインスタンス間で共有される
instance_b.print_val()

# コンストラクタ
# オブジェクトをインスタンス化する際に呼び出されるメソッド

class SampleClass:
     # コンストラクタ
    def __init__(self, msg, name =None):
        print("コンストラクタが呼ばれました")
        # インスタンス変数
        self.msg = msg 
        self.name = name
    
    # デストラクター
    # インスタンス削除に呼び出される
    def __del__(self):
        print('デストラクタが実行されました')
        print('name = {}'.format(self.name))

    def print_msg(self):# インスタンスメソッド
        print(self.msg)

    def print_name(self):# インスタンスメソッド
        print(self.name)

var_1 = SampleClass("駆逐してやる！","エレン")
# インスランス変数の表示
var_1.print_msg()
var_1.print_name()
del var_1 # インスタンス削除 -> デストラクターの呼び出し

# 各種メソッド
class MyClass:
    class_name = "World" # クラス変数

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_name_age(self): # インスタンスメソッド
        print("インスタンスメソッド実行")
        print('name = {}, age = {}'.format(self.name, self.age))
    # クラスメソッド
    # クラスをインスタンス化せずに実行
    @classmethod
    def print_class_name(cls,msg): # cls = MyClass
        print("クラスメソッド実行")
        print("Hello " + cls.class_name)
        print(msg)
        # print(name) コンストラクタの変数は呼び出せない(インスタンス変数)

    # スタティックメソッド
    # 普通の関数 クラス変数やインスタンス変数にアクセスできない
    @staticmethod
    def print_msg(msg):
        print("スタティックメソッド実行")
        print(msg)
MyClass.print_class_name('こんにちは')
man =  MyClass("エレン",18)
man.print_name_age()
man.print_msg("hello static") # スタティック呼び出し

# 特殊メソッド
class Human:
    def __init__(self,name,age,phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
    
    def __str__(self): # 文字列型変換
        # return 'Human'
        return self.name + ',' + str(self.age) + "," + self.phone_number
    
    def __eq__(self,other): # == で呼ばれる
        return (self.name == other.name) and (self.phone_number == other.phone_number) 

    def __hash__(self): # ハッシュで返す
        return hash(self.name +  self.phone_number)
    
    def __bool__(self): # ifで呼ばれる
        return True if self.age > 20 else False

    def __len__(self): # len()で呼ばれる
        return len(self.name)
            
man = Human('Rainer',20,'09076542234')
man2 = Human('Rainer',25,'09076542234')
man3 = Human('Eren',25,'08076542234')
print(man)
print(man == man2) # True(nameとphone_numberが同じだから)
print(hash('Mikasa')) # ハッシュ化する
set_man = {man,man2,man3}
for x in set_man:
    print(x)
    # 出力(man,man2は重複しているので片方のみ出力)
    # Eren,25,08076542234
    # Rainer,20,09076542234

if man:
    print("manはTrue")
if man2:
    print("man2はTrue")

print(len(man3)) # 4