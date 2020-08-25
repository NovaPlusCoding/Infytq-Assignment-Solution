#PF-Prac-11
def find_upper_and_lower(sentence):
    u_count, l_count = 0, 0
    for i in sentence:
        if i.isupper():
            u_count += 1
        if i.islower():
            l_count += 1
    return [u_count,l_count]

sentence="Come Here"
print(find_upper_and_lower(sentence))
