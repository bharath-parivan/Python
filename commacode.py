lis=[]

n=int(input("Enter how many list elements"))
print("Enter the elements")
for i in range (0,n):
	inp=input()
	lis+=[inp]

print("Before inserting comma_code\n",lis)\

new_string = ''
for k in lis:
    new_string = new_string + (k)
    if lis.index(k) == (len(lis)-2):
        new_string = new_string + ', and '
    elif lis.index(k) == (len(lis)-1):
        new_string = new_string
    else:
        new_string = new_string + ', '
print( new_string)

