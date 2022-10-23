t=int(input())
while(t):
    t-=1
    x1,y1,x2,y2=map(int,input().split())
    print(min((x1+y1),(x2+y2)))