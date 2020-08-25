#Prac-30
def new_file_pattern(old_file_name):
    with open(old_file_name, 'r') as f:
        list_lines = f.readlines()
        number, string = 1, ''
        for i in list_lines:
            string += str(number) + '.' + i
            number += 1
    new_file_name = 'newfile.txt'
    with open(new_file_name,'w') as file:
        file.write(string)
    return new_file_name

with open('file.txt','w') as f:
    f.write("This is first line.\nThis is Second line.\nThis is third line.\nThis is last line.")
with open (new_file_pattern('file.txt'),'r') as f:
    print(f.read())
