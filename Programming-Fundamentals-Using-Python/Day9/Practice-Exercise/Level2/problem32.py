#PF-Prac-32
import math
def check_squares(number):
    flag = False
    for i in range(int(math.sqrt(number))+1):
        for j in range(i+1,int(math.sqrt(number))+1):
            if i ** 2 + j ** 2 == number:
                flag =True
    return flag


number=68
print(check_squares(number))
