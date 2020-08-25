#PF-Prac-26
def check_occurence(string):
    return string.lower().count('mat') == string.lower().count('jet')

string="Jet on the Mat but mat is too long"
print(check_occurence(string))
