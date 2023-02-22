# 0011 1100 - 60
# 0000 1101 - 30

# 0011 1100 - 60
# AND
# 0000 1101 - 30
# 0000 1100 - 8+ 4-> 12


# 0011 1100 - 60
# OR
# 0000 1101 - 30
# 0011 1101 - 1+0+4+8+16+32 -> 61

# 0011 1100 - 60
# XOR
# 0000 1101 - 30
# 0011 0001 - 1+0+0+0+16+32 - 49

# 0011 1100
# ~0011 1100 = 1100 0011 

#a = 0011 1100 
#c = a << 2;       # 240 = 1111 0000





#!/usr/bin/python3

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;        # 12 = 0000 1100
print ("result of AND is ", c,':',bin(c))

c = a | b;        # 61 = 0011 1101 
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        # 49 = 0011 0001
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           # -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       # 240 = 1111 0000
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       # 15 = 0000 1111
print ("result of RIGHT SHIFT is ", c,':',bin(c))