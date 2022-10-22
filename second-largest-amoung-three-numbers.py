
t=int(input())
while(t):
    t-=1
    l=list(map(int,input().split()))
    l.sort()
    print(l[1])
