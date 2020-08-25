#PF-Prac-16
def rotate_list(input_list,n):
    another_list = input_list[:]
    for i in range(n % len(input_list)):
        another_list = another_list[-1:]+another_list[:-1]
    return another_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)
