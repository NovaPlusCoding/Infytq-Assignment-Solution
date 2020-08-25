#PF-Prac-44
def check_correct_depth(input_list, depth=0):
    count,flag = 0, True
    for i in input_list:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        else:
            if int(i) != count:
                flag = False
    return flag

input_list1=list('(1)')
input_list2=list('(2)')
input_list3=list('((2)((3)))')
input_list4=list('((2)(3))')
input_list5=list('((3)(2))')
input_list6=list('(((3)((4))(3))(2)((3)))')
output=check_correct_depth(input_list5)
print("Input list:",input_list5)
print(output)
