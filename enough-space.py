
t=int(input())
while(t):
    t-=1
    n,x,y=map(int,input().split())
    if(x+y*2<=n):print("YES")
    else:print("NO")
    
    