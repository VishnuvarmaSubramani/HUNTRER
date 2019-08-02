N,K= map(int,input().split())
LIS = list(map(int,input().split()))
LIS = sorted(LIS,reverse =True)
print(LIS[K-1])
