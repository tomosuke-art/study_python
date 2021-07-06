# ビット演算
a = 0b10101001
b = 0b10001100

print("AND",bin(a&b))
print("OR",bin(a|b))
print("XOR",bin(a^b))
print('~0',~0)
print('~1',~1)
print('~-1',~-1)
print('~-2',~-2)
print('0b10101001<<1',bin(a<<1))
print('0b10101001>>2',bin(b>>2))

# 出力
"""
AND 0b10001000
OR 0b10101101
XOR 0b100101
~0 -1
~1 -2
~-1 0
~-2 1
0b10101001<<1 0b101010010
0b10101001>>2 0b100011
"""
