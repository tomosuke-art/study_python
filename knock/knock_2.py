# クラス基礎
# knock38
class Person():
  def say_hello(self,nationality):
    print("こんにちは、私の国籍は" + nationality + "です")
name = Person()
name.say_hello("japan")

# knock38別解 + knock39(コンストラクタの設定)
class Person():
  nationality = "japan"
  # コンストラクタの設定
  def __init__(self,name):
      self.name = name
  def say_hello(self):
    print(f"こんにちは、私の国籍は,{self.nationality}です")
  def say_my_name(self):
    print(f"私の名前は{self.name}です")
nakagawa = Person("中川")
nakagawa.say_my_name()
# person = Person()
# person.say_hello()

# knock40
# クラスの継承
class Kid(Person):
  # 上メソッド書き
  def say_hello(self,age):
    print(f"私の名前は{self.name}です。年齢は{age}歳です")
kid = Kid("エレン")
kid.say_hello(15)