#PF-Prac-38
def build_index_grid(rows, columns):
    result_list =[]
    for i in range(rows):
        an_list = []
        for j in range(columns):
            an_list.append('{},{}'.format(i,j))
        result_list.append(an_list)
    return result_list

rows=4
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)
