input()
T=sorted(sorted(map(int,input().split()),reverse=True),key=abs)
print(T and T[0] or 0)
