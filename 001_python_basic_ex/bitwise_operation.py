x = 4  # which means 0000 0100
y = 1  # which means 0000 0001
  
  # now we apply the bitwise operation

a = x & y  # the result for '&' operation is [0000 0000] = 0   {and}
b = x | y  # the result for '|' operation is [0000 0101] = 5   {or}
c = ~x     # the result for '~' operation is [1111 1011] = 251 = -5   {neg}
d = x ^ 5  # the result for '^' operation is [0000 0101] = 1 bcoz 5 = [0000 0101]  {xor}
e = x >> 2 # the result for '>>'operation is shifting right by 2 bit which is [4 // 2^2] = 1
f = x << 2 # the result for '<<'operation is shifting left by 2 bit which is [4 * 2^2] = 16

print(a, b, c, d, e, f)
