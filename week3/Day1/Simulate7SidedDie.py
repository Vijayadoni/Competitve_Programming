import random


def rand5():
    return random.randint(1, 5)


def rand7():

    # Implement rand7() using rand5()
    while (True):
    	i = (rand5()-1)*5+rand5()
    	if i<=21:
    		return (i)%7+1
    

print ('Rolling 7-sided die...')
print (rand7())