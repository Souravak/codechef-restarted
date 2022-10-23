t=int(input())
while(t):
    t-=1
    n,x,k=map(int,input().split())
    if(k>=x*n):print("YES")
    else:print("NO")