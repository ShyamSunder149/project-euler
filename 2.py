a = 1
b = 2
val = 4000000
s = 2 
while b < val :
    c = a + b
    if c%2 == 0 : s += c 
    a = b
    b = c
print(s)

