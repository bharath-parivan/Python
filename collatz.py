
print("\t \t \t NAME: BHARATH PARIVAN \n\t \t \t USN: 1AY24AI018 \n\t \t \t SEC:'M'")
n=int(input("Enter a number"))
seq=[n]
while n!=1:
	if n%2==0:
		n=n//2
	else:
		n=3*n+1
	seq.append(n)
print(seq)