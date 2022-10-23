t=int(input())
while(t):
    t-=1
    x,y=map(int,input().split())
    print(min(x*3,y*2))