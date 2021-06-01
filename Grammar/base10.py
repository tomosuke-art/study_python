## ファイル入力
file_path = 'input.csv'
f = open(file_path, mode = 'r', encoding = 'utf-8')

# line = f.read() # 中身全体
# print(line)

# lines = f.readlines() # リストで表示
# print(lines)

# for x in lines:
#     print(x.rstrip('\n')) # 改行して一つづつ表示

line = f.readline()
while (line := f.readline()): # セイウチ演算子で1行で
    print(line.rstrip('\n'))
    # line = f.readline()

f.close() # ファイル閉じる 以降は実行されない
# ファイル開いてる -> メモリを食う、他の処理で開けない
# with
with open(file_path,mode='r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

print(f.read()) # ファイルは閉じられているので実行されない

