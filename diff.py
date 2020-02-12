l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
L1=[x for x in l1 if x not in l2]
print('Difference = ',L1)
[L1.append(i) for i in l2 if i not in l1]
print('Symm. Diff = ',L1)
