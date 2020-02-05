a=int(input("Enter Value Of a "))
b=int(input("Enter Value Of  b "))
c=int(input("Enter Value Of  c "))
D = b**2 - 4*a*c
if D < 0 : 
	print("No Roots")
if D > 0 :
	print((-b + D**0.5)/(2*a))
	print((-b - D**0.5)/(2*a))

