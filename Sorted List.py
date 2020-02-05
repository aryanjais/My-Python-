l=[]
while 1 :
	a=input("Enter The Item : ")
	if a!='' :
		l.append(a)
	else :
		q=input("Do You Want To Continue : Y/N ?")
		if  q.lower() == 'n' :
			break
l.sort(reverse=True,key=len)
print(l)
