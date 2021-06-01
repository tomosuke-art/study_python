## ファイル出力(書き込み)
file_path_2 = 'output.csv'
f = open(file_path_2,mode = 'w',encoding='utf-8',newline='\n')
f.write('一花\n二乃\n美久\n四葉\n五月\n')
f.close()
# 再度書き込み(上書き mode=w,追記 mode=a)
with open(file_path_2,mode='a',encoding='utf-8',newline='\n') as f:
    list_a=[
        ['エレン ','ミカサ ','アルミン '],
        ['進撃の巨人 ','鎧の巨人 ','超大型巨人 ']
    ]
    for x in list_a:
        f.write('\n')
        f.write(','.join(x))

    #f.writelines(list_a[1])


## with
class WithTest:
    def __init__(self,file_name):
        print('init called')
        self.__file_name = file_name
    def __enter__(self):
        print('enter called')
        self.__file = open(self.__file_name, mode='w', encoding='utf-8')
        return self # -> t に格納
    
    def write(self,msg):
        self.__file.write(msg)

    def __exit__(self,exc_type,exc_val,traceback): # 引数三つ必要
        print('exit called') # 最後に呼ばれる
        self.__file.close()
with WithTest('output.txt') as t:
    print('withのなか')
    t.write('上杉風太郎') # output.txtを作成