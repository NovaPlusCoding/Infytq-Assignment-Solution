def sum_of_elements(num_list,number):
    l=[]
    for i,x in enumerate(num_list):
        if x==number:
                if i!=0:
                    l.append(num_list[i-1])
                if i!=len(num_list)-1:
                    l.append(num_list[i+1])
    result = sum(num_list) - (num_list.count(number)* number + sum(l))
    return result

num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))
