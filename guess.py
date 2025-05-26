print("\t \t \t NAME: ANEESH.P \n\t \t \t USN: 1AY24AI008 \n\t \t \t SEC:'M'")

import random as rn
n=int(input("guess a number from 1 to 100 : "))
r=rn.randint(1,3)
k=10
for i in range(1,10):
	print("Random number = ",r)
	if (n==r):
		print("You have guessed the number correctly")
		bool=input("Do you want to continue?[Enter yes or no]")
		if(bool=="yes"):
			n=int(input("guess a number from 1 to 100 : "))
			r=rn.randint(1,3)
		else:
			break
	else:
		print("Guessed the wrong number!! >0< ")
		k-=1
		print("Try again {You have",k,"chances left!!}")
		bool=input("Do you want to continue?[Enter yes or no]")
		if(bool=="yes"):
			n=int(input("guess a number from 1 to 100 : "))
			r=rn.randint(1,3)
		else:
			break
