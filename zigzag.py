print("\t \t \t NAME: BHARATH PARIVAN\n\t \t \t USN: 1AY24AI018 \n\t \t \t SEC:'M'")

r=int(input("Enter number of rows"))
c=int(input("Enter number of columns"))

for i in range(r):
	for j in range(c):
		if(i+j)%(r-1)==0 :
			print("-",end="")
		else:
			print(" ",end="")
	print()
