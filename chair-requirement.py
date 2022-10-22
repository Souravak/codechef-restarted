t=int(input())
while(t):
    t-=1
    x,y=map(int,input().split())
    print(max((x-y),0))