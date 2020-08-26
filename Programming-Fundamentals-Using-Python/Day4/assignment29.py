
#PF-Assgn-29
def calculate(distance,no_of_passengers):
    ticket=no_of_passengers*80
    mile=(distance)/10
    fuel=mile*70
    earning=ticket-fuel
    if earning>0:
        return earning
    else:
        return -1
        
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
