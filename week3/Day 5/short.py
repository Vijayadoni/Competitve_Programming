def Base_convert(string):
	dic={}
	for i in range(len(str1)):
		dic[i]=str1[i]
	return dic


x = 7
y={}
z={}
count=0
base=Base_convert("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")


def URL_Shortnermethod(Given_URL):
	if (Given_URL in z):
		print("ShortURL Exists"+z[Given_URL])
		return
	global count
	s=""
	k=count
	count+=1

	if (k==0):
		s="0000000"
		if (s not in y):
			y[s]=Given_URL
			z[Given_URL]=s
			print("short URL for "+Given_URL+" is https://ca.ke/"+s)
			return

	while(k!=0):
		s=base[k%62]+s
		k=k//62
	l=len(s)

	if (l<x):
		for i in range(x-l):
			s="0"+s

	if (s not in y):
		y[s]=Given_URL
		z[Given_URL]=s

	print("Shortened URL for "+Given_URL+" is https://ca.ke/"+s)

while (True):
	print("\n\t1)Generate ShortURL\n\t2)Redirect ShortURL\n\t3)Stop\n\tYour option:",end="")
	i=int(input())
	if (i==1):
		Given_URL=input("Enter URL: ")
		URL_Shortnermethod(Given_URL)
	elif (i==2):
		Correct_URL=input("Enter a short URL: ")
		if y.get(Correct_URL,None) is not None:
			print("Redirect to "+y[Correct_URL])
		else:
			print("URL does not exist")
	elif(i==3):
		print("Thank you for using us")
		break
	else:
		print("Please enter valid Input")