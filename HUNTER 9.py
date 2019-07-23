N=int(input())
LIS=list(map(int,input().split()))
X=len(LIS)
large=max(LIS)
A,B=0,0
for i in range(0,X-1):
 for j in range(i+1,X):
  if abs(LIS[i]+LIS[j])< large:
   A,B=LIS[i],LIS[j]
   large=abs(A+B)
print(A, B)
