from itertools import permutations
N=input()
X=permutations(N)
S=[]
for i in list(X):
        N="".join(i)
        if N not in S:
             S.append(N)
for i in S:
      print(i)
