l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
L1=[x for x in l1 if x in l2]
print(L1)
L2=[l1.append(x) for x in l2 if x not in l1]
print(l1)
