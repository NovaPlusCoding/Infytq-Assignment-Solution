#PF-Prac-7
def seed_no(number,ref_no):
    flag = False
    product = number
    list1 = [int(x) for x in str(number)]
    for x in list1:
        product *= x
    if product == ref_no:
        flag = True
    return flag

number=123
ref_no=738
print(seed_no(number,ref_no))
