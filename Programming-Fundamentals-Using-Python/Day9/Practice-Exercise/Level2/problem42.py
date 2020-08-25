#PF-Prac-42
def maxvalue_in_column(pixel_grid):
    row,column = len(pixel_grid), len(pixel_grid[0])
    n_list = []
    for i in range(column):
        list1 = []
        for element in pixel_grid:
            list1.append(element[i])
        n_list.append(list1)
    result_list = [max(i) for i in n_list]
    return result_list

pixel_grid=[[ 4, 2, 3],
            [16, 5, 0],
            [ 3, 200, 6],
            [ 0, 10, 12]]
pixel_grid1=[[ 4 ],
             [ 16 ],
             [ 3 ],
             [ 0 ]]
pixel_grid2=[[ 4, 2, 3]]
pixel_grid3= [[6]]

print("Pixel grid is:")
for i in pixel_grid:
    print(i)
output=maxvalue_in_column(pixel_grid)
print("The maximum values of each column are:",output)
