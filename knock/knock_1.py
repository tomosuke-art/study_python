# knock21
dictionary = {
  "A":"北村匠海",
  "B":"あいみょん ",
  "C":"尾崎世界観",
  "D":"YOASOBI",
  "E":"椎名林檎",
}
# キーのみ表示
print(dictionary.keys())
# 全てのキーと値の表示
print(dictionary.items())
# 要素検索 C,Eに対応する値
print(dictionary["C"])
print(dictionary["E"])

# knock24
a = 2
# aが0以上10未満かつ偶数
if 0 <= a < 10 and a % 2 == 0:
  print("一桁の偶数です")
elif a < 0 and a % 2 == 1:
  print("負の奇数です")
else:
  print("整数です")

# knock28
for i in range(10):
  # 3の時処理をスキップ
  if i == 3:
    continue
  print(i)

# knock29
# 複数のリストから同時に出力
lasts = ["エレン","アルミン","ミカサ"]
firsts = ["・イェーガー","・アルレルト","・アッカーマン"]

for last ,first in zip(lasts, firsts):
  print(last + first)
# 要素とインデックスを同時に取得
for i,name in enumerate(lasts):
  print(str(i) + "番目は" + name + "です")

# knock31
# 内包表記 9未満の2の倍数
numbers = [2 * i for i in range(5)]
print(numbers)
nums = []
for i in range(9):
  if i % 2 == 0:
    nums.append(i)
print(nums)

# knock32
# 例外処理
num = 0
try:
    print(f"計算結果:{10/num}")
# エラー後の処理
# except:
#   print("エラー")

# エラーごとに対処法を変えることができる(以下knock34)
except ZeroDivisionError as e:
    print(e)

# knock34
# エラーごとに処理を変更
def divide(a,b):
  try:
    print(f"計算結果:{a/b}")
  except ZeroDivisionError as e:
    print(e)
  except TypeError as e:
    print(e)
  # 正常に処理ができた時
  else:
    print("正常に終了しました")
  # 例外が発生してもしなくても処理する時
  finally:
    print("全ての処理が終了しました")
divide(10,"zero")
divide(10,0)
divide(10,2)