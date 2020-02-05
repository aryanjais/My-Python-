a=int(input("Enter a number : "))
s=0
for n in range (1, a+1):
	if a%n==0 :
		s=s+1
if s==2 :
	print("Prime number")
if s!=2 :
	print("not Prime number")
	

