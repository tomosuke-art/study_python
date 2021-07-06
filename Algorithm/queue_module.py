# スタックとキューを扱うqueueモジュール
import queue

MAX = 10

print('キュー')
q = queue.Queue() # Queueオブジェクトを用意
for i in range(MAX):
    q.put(i) # キューにiの値を代入
for i in range(MAX):
    print(q.get(),end="->")

print('\n')
print('スタック')
s = queue.LifoQueue() # LifoQueueオブジェクトを用意
for i in range(MAX):
    s.put(i) # スタックにiの値を代入
for i in range(MAX):
    print(s.get(),end="->")