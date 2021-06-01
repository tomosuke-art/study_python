# ファイル操作
# knock42
# ファイル操作
file = open('sample.txt')
text = file.read()
file.close()
# sample.txtを取得
print(text)

# knock43
# with構文 
with open('sample.txt','r') as f: # 'r' = 読み込み
  text = f.read()
print(text)

# JSONファイルの場合(ファイルはない)
# import json
# with open('sample.json','r') as f: # 'r' = 読み込み
#   data = json.load(f)
# print(data)

# OS操作
# カレントディレクトリのファイルを取得
import os
for curDir , dirs, files in os.walk('.'):
  for file in files:
    print(f'{curDir}/{file}')

lists = os.listdir('.')
print(lists)  

# knock47
# 絶対パスの取得,
path = os.path.abspath('./knock_3.py')
print(path)
# ファイル名の取得
name = os.path.basename('./knock_3.py')
print(name)
# ファイル・ディレクトリの存在確認
jage = os.path.exists('xyz')
print(jage) # False