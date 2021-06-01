# オブジェクト指向(継承、ポリモーフィズム)

#クラスの継承
class Preson: # 親クラス
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greeting(self):
        print('hello {}'.format(self.name))
    def say_age(self):
        print('{} years old'.format(self.age))

class Employee(Preson): # 親クラスの機能を継承
    def __init__(self,name,age,number):
        super().__init__(name,age) # 親クラスのname.ageの初期化
        self.number = number

    def say_number(self):
        print('my number is = {}'.format(self.number))

    def greeting(self): # オーバーライド
        super().greeting()
        print('I\'m employee phone_number = {}'.format(self.number))

    # def greeting(self,age): # オーバーロード 上の関数を上書く
    #     print('オーバーロード')

women = Employee('サシャ・ブラウス',18,'080-4459-0129')
women.greeting()
women.say_age()
women.say_number()


# 多重継承
class ClassA:
    def __init__(self,name):
        self.a_name = name

    def print_a(self):
        print('ClassAのメソッド実行')
        print('a = {}'.format(self.a_name))

    def print_hi(self):
        print('A hi')

class ClassB:

    def __init__(self,name):
        self.b_name = name

    def print_b(self):
        print('ClassBのメソッド実行')
        print('b = {}'.format(self.b_name))

    def print_hi(self):
        print('B hi')

class NewClass(ClassA,ClassB):
    def __init__(self,a_name,b_name,name):
        ClassA.__init__(self,a_name)
        ClassB.__init__(self,b_name)
        self.name = name

    def print_new_name(self):
        print('NewClassのメソッド実行')
        print('name = {}'.format(self.name))

    def print_hi(self): # オーバーライド
        ClassA.print_hi(self)
        ClassB.print_hi(self)
        print('NewClass hi')
sample = NewClass("Netflix","Amazon","Disney+") # A,B,New
sample.print_a()
sample.print_b()
sample.print_new_name()
sample.print_hi() # オーバーライドしたものを実行

# メタクラス
# クラスの再定義するクラス、クラスの検証する際に用いる
class MetaException(Exception):
    pass

class Meta1(type): # type(デフォルトのメタクラス)
    def __new__(metacls,name,bases,class_dict):
        print('metacls = {}'.format(metacls))
        print('name = {}'.format(name)) # ClassA
        print('bases = {}'.format(bases)) # 継承するクラス
        print('class_dict = {}'.format(class_dict))
        if 'my_var' not in class_dict.keys():
            raise MetaException('my_varを定義してください')
        for base in bases: # 継承クラスをあらわす
            if isinstance(base,Meta1):
                raise MetaException('継承できません')
        return super().__new__(metacls,name,bases,class_dict)

class ClassC(metaclass = Meta1):
    a = '123'
    my_var = 'ABC'
    pass

class subClassC(ClassC):
    pass
