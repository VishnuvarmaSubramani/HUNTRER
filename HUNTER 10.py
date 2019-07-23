N,M=map(int,input().split())
A=list(input().split())
B=list(input().split())
if (set(B) <= set(A)):
    print("YES")
else:
    print("NO")
