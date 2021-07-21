with open('first.txt') as f1,open('second.txt') as f2:
	for l1,l2 in zip(f1,f2):
		# print(l1+l2)
		l1=l1.strip()
		l2=l2.strip()
		print(l1+l2)
