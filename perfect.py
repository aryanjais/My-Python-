a=int(input("Enter a no."))
s=0
for n in range (1,a) :
	if a%n==0 :
		s+=n
if s==a :
	print ("Perfect No.")
else :
	print("Not Perfect")	
