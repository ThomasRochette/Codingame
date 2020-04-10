a,b,x,y=map(int,input().split())
while True:
    d=("S" if b>y else "N" if b<y else "")+("E" if a>x else "W" if a<x else "")
    y=y+1 if "S" in d else y-1 if "N" in d else y
    x=x+1 if "E" in d else x-1 if "W" in d else x
    print(d)
    
