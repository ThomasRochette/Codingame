a,b,x,y=map(int,input().split())
while True:
    d=(b>y and "S" or b<y and "N" or "")+(a>x and "E" or a<x and "W" or "")
    y="S" in d and y+1 or "N" in d and y-1 or y
    x="E" in d and x+1 or "W" in d and x-1 or x
    print(d)
    
