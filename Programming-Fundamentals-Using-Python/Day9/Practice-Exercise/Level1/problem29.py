#PF-Prac-29
def exchange_list(number_list):
    number_list = number_list[len(number_list)//2:][::-1] + number_list[:len(number_list)//2]
    return number_list
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
