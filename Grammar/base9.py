# ポリモーフィズム (多態性)
# 同じ名前のメソッドを複数のクラスで使用できるようにする
# サブクラスを複数作成し、同じメソッドを定義して呼び出す際にどのクラスか意識せずに呼び出す

from abc import abstractmethod, ABCMeta

class Human(metaclass = ABCMeta): #親クラス(metaclass = 抽象クラス)
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def say_something(self):
        pass # 中身は定義しない
    def say_name(self):
        print(self.name)
# 同様のメソッドを持つ
class Woman(Human):
    def say_something(self):
        print('女性 : 名前 = {}'.format(self.name))

class Man(Human):
    def say_something(self):
        print('男性 : 名前 = {}'.format(self.name))

num =  input('0か1を入力してください:')
if num == '0': # Manクラスのsay_something()を実行
    human = Man('Eren')
elif num == '1':# Womanクラスのsay_something()を実行
    human = Woman('Mikasa')
else:
    print('間違っています')
human.say_something()

# プライベート変数
# 外部からアクセスのできない変数
# ゲッター、セッターを利用してアクセスする
class People:
    __class_val = 'Human'
    def __init__(self,name,age):
        self.__name = name # private変数 -> 外部からアクセスできない
        self.age = age
    
    def print_msg(self):
        print('name = {},age = {}'.format(self.__name,self.age))

human = People("リヴァイ",20)
human.print_msg() # アクセス可能

# カプセル化(クラスの外部から変数が見えないようにする)
# setter,getter(プライベート変数にアクセス)
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print('getter nameを呼び出しました')
        return self.__name

    def get_age(self):
        print('getter ageを呼び出しました')
        return self.__age

    def set_name(self,name):
        print('setter nameを呼び出しました')
        self.__name = name
    
    def set_age(self,age):
        print('setter ageを呼び出しました')
        self.__age = age
    
    name = property(get_name,set_name) # nameを指定するとget name, set nameが呼ばれる
    age = property(get_age,set_age) # ageを指定するとget age, set ageが呼ばれる

    def print_msg(self):
        print(self.name,self.age)

human = Person('エルヴィン',25)
human.name = "スミス" # set_name()を呼び出す
# getter呼び出し
print(human.name)
print(human.age)

human.print_msg() # -> スミス 25
# getter setter その２
class Pyman:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    # getter
    @property
    def name(self): 
        print('getter nameが呼ばれました')
        return self.__name
    
    @property
    def age(self):
        print('getter ageが呼ばれました')
        return self.__age

    # setter
    @name.setter
    def name(self,name):
        print('settre nameが呼ばれました')
        self.__name =  name
    
    @age.setter
    def age(self,age):
        print('setter ageが呼ばれました')
        if age < 0:
            print('0以上の値を設定してください')
            return
        self.__age = age

pyman =  Pyman("python",22)
pyman.name = "ジョブズ" # setter name
print(pyman.name) # getter name
pyman.age = -1 # 0以上の値を設定してください


# 演習問題(継承とポリモーフィズム)
class Animals(metaclass = ABCMeta):
    @abstractmethod
    def speak(self):
        pass
# speak()をそれぞれオーバーライド
class Dog(Animals):
    def speak(self):
        print('ワン')

class Cat(Animals):
    def speak(self):
        print('ニャー')

class Sheep(Animals):
    def speak(self):
        print('メー')

class Other(Animals):
    def speak(self):
        print('そんな動物いないよ')

number = input('好きな動物は？ 1:犬, 2: 猫, 3: 羊')
if number == '1':
    animal = Dog()
elif number == '2':
    animal = Cat()
elif number == '3':
    animal  =Sheep()
else:
    animal = Other()

animal.speak() # speakの呼び出し(ポリモーフィズム)

