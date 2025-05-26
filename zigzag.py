print("\t \t \t NAME: ANEESH.P \n\t \t \t USN: 1AY24AI008 \n\t \t \t SEC:'M'")

r=int(input("Enter number of rows"))
c=int(input("Enter number of columns"))

for i in range(r):
	for j in range(c):
		if(i+j)%(r-1)==0 :
			print("-",end="")
		else:
			print(" ",end="")
	print()
