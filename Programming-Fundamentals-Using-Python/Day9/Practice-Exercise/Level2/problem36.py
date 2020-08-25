# PF-Prac-36
def find_target_positions(input_string, target_word):
    target_list = []
    # split_inp = input_string.split()
    idx = input_string
    for i, word in enumerate(idx):
        if word == target_word:
            target_list.append(i)
    return target_list

def find_inverted_index(input_string):
    target_dict = {}
    split_inp = input_string.split()
    for k in split_inp:
        target_dict.update({k: find_target_positions(split_inp, k)})
    return target_dict

input_string = "we dont need no education we dont need no thought control no we dont"
result_dict = find_inverted_index(input_string)
print(result_dict)
