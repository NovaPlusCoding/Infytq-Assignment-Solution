def adding_ing(string):
    if len(string)>=3:
        if string.endswith('ing'):
            new_string = string + 'ly'
        else:
            new_string = string + 'ing'
    else:
        new_string = string
    return new_string

string = input('Enter any string : ')
print(adding_ing(string))
