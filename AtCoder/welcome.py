# practiceA
n = int(input())
num = input().split()
s = input()
sum = n + int(num[0]) + int(num[1])
print(sum,s)

# ABC086A
num = input().split()
a = int(num[0])
b = int(num[1])
if (a*b) % 2 == 0:
  print("Even")
else:
  print("Odd")

# ABC081A
num = input().split()
count = 0
for n in num[0]:
  if int(n) == 1:
    count += 1
print(count)

# ABC081B
n = int(input())
count = 0
flag = 0
for i in range(n):
  num = input().split()
  for j in num:
    if int(j) % 2 == 0:    
       flag += 1
       if flag == 3:
         count += 1
print(count)

