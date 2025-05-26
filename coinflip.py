import random as r
n=int(input("How many flips you wanna do?"))
lis=[]
for i in range(0,n):
	h_t =r.choice(['H','T'])
	lis+=[h_t]
a=1
grt=1
for j in range(1,n):
	if lis[j]==lis[j-1]:
		a+=1
		grt=max(a,grt)
	else:
		a=1
print(f"All Flips >> {lis}")
print(f"You have a streak offfff....... {grt}")