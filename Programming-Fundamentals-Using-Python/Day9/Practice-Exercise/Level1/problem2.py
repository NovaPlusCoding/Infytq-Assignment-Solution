# PF-Prac-2
def bracket_pattern(input_str):
    return input_str.count('(') == input_str.count(')') and input_str.startswith('(') and input_str.endswith(')')

input_str = "(())("
print(bracket_pattern(input_str))
