m=''.join(bin(ord(x))[2:].zfill(7) for x in input())
a,b='',''
for c in m:
    if c=="1"!=b:
        a+=" 0 "
        b="1"
    elif c=="0"!=b:
        a+=" 00 "
        b="0"
    a+= "0"
print(a.strip())
