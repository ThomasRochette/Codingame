m=''.join(bin(ord(x))[2:].zfill(7) for x in input())
a,b='',''
for c in m:
    (a,b)=(c=="1"!=b)and(a+" 0 ","1")or(c=="0"!=b)and(a+" 00 ","0")or(a,b)
    a+="0"
print(a.strip())
