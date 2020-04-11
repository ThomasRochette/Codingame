n = int(input())
t=list(map(int,input().split()))
m=min(list(map(abs,t))) if len(t)!=0 else 0
print(m if m in t else "-"+str(m) if m!=0 else "0")
