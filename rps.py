print("\t \t \t NAME: ANEESH.P \n\t \t \t USN: 1AY24AI008 \n\t \t \t SEC:'M'")

import random
print("\tROCK , PAPER , SCISSORS")
w=0
l=0
t=0
while True:
	print(w,"WINS",l,"LOSSES",t,"TIES")
	move=input("Enter your move : (r)ock (p)aper (s)cissors or (q)uit : ")
	com=random.randint(0,2)
	if(move=="r"):
		print("ROCK versus")
		if(com==0):
			print("ROCK \n IT IS A TIE!!")
			t+=1
		elif (com==1):
			print("PAPER \n YOU WON!!")
			w+=1
		else:
			print("SCISSORS \n SORRY YOU LOST TRY AGAIN!")
			l+=1
		print(w,"WINS",l,"LOSSES",t,"TIES")
		
	elif(move=="p"):
		print("PAPER versus")
		if(com==0):
			print("ROCK \n YOU WON!!")
			w+=1
		elif (com==1):
			print("PAPER\n IT IS A TIE!!")
			t+=1
		else:
			print("SCISSORS \n SORRY YOU LOST TRY AGAIN!")
			l+=1
		print(w,"WINS",l,"LOSSES",t,"TIES")
	elif(move=="s"):
		print("SCISSORS versus")
		if(com==0):
			print("ROCK \n SORRY YOU LOST TRY AGAIN!")
			l+=1
		elif (com==1):
			print("PAPER \n YOU WON!!")
			w+=1
		else:
			print("SCISSORS\n IT IS A TIE!!")
			t+=1
		print(w,"WINS",l,"LOSSES",t,"TIES")
	else:
		print('"HOPE YOU ENJOYED PLAYING THE GAME COME AGAIN"')
		break
		
		