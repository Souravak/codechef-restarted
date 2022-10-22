# cook your dish here
t=int(input())
while(t):
    t-=1 
    n,k=map(int,input().split())
    if n>=k :print("NO")
    else:print("YES")