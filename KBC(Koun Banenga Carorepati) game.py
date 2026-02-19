import random

ques = ["what is the capital of india",
		"what is the national animal of india",
		"what mean bhat in english",
		"what is the capital of france",
		"what is the V2 form of sit"]

ops = ["(a) delhi (b) mumbai (c) kolkata (d) france",
		"(a) lion (b) fox (c)tiger (d) peacock",
		"(a) cake (b) rice (c) puffel (d) frenki",
		"(a) woshington (b) algeria (c) paris (d) delhi",
		"(a) sat (b) sit (c) siten (d) sot"]



ans = ["a", "c", "b", "c", "a"]
idxes = []
am = 1


while True:


	if(len(idxes) == len(ques)):
		print()
		print()
		print("Aap", am, "crore jit chuke hai")
		break


	r = random.randint(0,len(ques)-1)
	if r in idxes:
		continue

	else:
		idxes.append(r)

	que = ques[r]
	
	opt = ops[r]
	an = ans[r]
	if(am == 1):

		print()
		print()
		print(am,"crore keliye aapka",am, "st sawal")

	elif(am == 2):

		print()
		print()
		print(am,"crore keliye aapka",am, "nd sawal")

	elif(am == 3):

		print()
		print()
		print(am,"crore keliye aapka",am, "rd sawal")

	else:

		print()
		print()
		print(am,"crore keliye aapka",am, "th sawal")

	


	print()
	print(que)
	print(opt)
	
	

	print()
	
		
	
	i = input("Aapka jawab kya hai ? : ")
	
	
	if i in an:
		print()
		print()
		print("Sahi jawab,",am,"crore.")
		am += 1
		print()
		print()
		

	
	else:
		print()
		print()
		print("Aap har chuke hai ! Sahi jawab", an,"tha.")
		print()
		print()

		break
	