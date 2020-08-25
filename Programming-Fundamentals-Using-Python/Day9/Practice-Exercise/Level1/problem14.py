#PF-Tryout
def find_five_digit():
	for i in range(10):
	    fourth = i
	    third = i+2
	    fifth = i+2
	    second = i+4
	    first = i+6
	    if third+fourth+fifth == first and (first+second+third+fourth + fifth) == 19:
	        print(int(str(first)+str(second)+str(third)+str(fourth) + str(fifth)))

find_five_digit()
