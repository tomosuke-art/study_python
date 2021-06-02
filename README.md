# Python
## 標準入力のやり方
#### 1行1データ  
```
# str型
s = input()
# int型
s = int(input())
```

#### (1,N)行列データ
・入力値が文字列  
<入力例>  
Eren Mikasa Armin  

```
# list型
s = input().split()
#出力
>>>print(s)
['Eren', 'Mikasa', 'Armin']

# 文字列型
A, B, C = input().split()

#出力
>>>print(A,B,C)
Eren Mikasa Armin
```

・入力値が整数  
<入力例>    
12 35  
```
A, B = map(int, input().split())

#出力
>>>print(A)
12
>>>print(A,B)
12 35
```

・入力値の整数がN個の場合  
<入力例>  
1 3 5 7 9 
```
# list型で取得
S = list(map(int,input().split()))
#出力
>>>print(S)
[1,3,5,7,9]
```

#### 一般行列データ
<入力例>  
(4,5)行列データ    
4 5  
1  3 5 7  
12 3 4 8  
8  9 0 45  
34 6 6 78  
12 3 5 55  

```
# リスト内包表記で
N, M = map(int,input().split()) 
#上から順にlistを読み込んでlistに格納していく。
a = [list(map(int, input().split())) for l in range(M)]
for x in a:
   print(*x)
   
# 出力
1  3 5 7  
12 3 4 8  
8  9 0 45  
34 6 6 78  
12 3 5 55  
```

## 用語
**オーバーライド**  
親クラスのメソッドを上書きして、新たに定義する  

**オーバーロード**  
引数や戻り値が異なるが名称が同一のメソッドを定義する  
Pythonでは利用できない  

**Django**  
・Pythonで最もよく利用されているwebフレームワーク  
・コードの自動生成機能があるので初心者は中身を理解できないまま開発してしまうことも  
・MTV(モデル・テンプレート・ビュー)と呼ばれる考え方を採用  