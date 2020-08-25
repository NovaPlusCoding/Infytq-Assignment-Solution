#PF-Tryout
def doublePreceding (values):
    if len(values) > 0:
        list1 = tuple(values)
        for idx in range(1, len(values)):
            values[idx] = 2 * l1st1[idx-1]
        values[0]=0
    return values

print(doublePreceding([3,8,2])) 
