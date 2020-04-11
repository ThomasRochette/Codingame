n=input()
for i in range(int(n)):
    l=input()
while True:
    x,y,hs,vs,f,r,p = map(int,input().split())
    print(vs<-39 and "0 4" or vs<10 and "0 3" or "0 0")
