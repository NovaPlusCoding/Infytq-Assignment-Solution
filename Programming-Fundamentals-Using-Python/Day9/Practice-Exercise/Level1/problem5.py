#PF-Prac-5
def count_digits_letters(sentence):
    letter_count, digit_count = 0, 0
    for each in sentence:
        if each.isalpha():
            letter_count += 1
        elif each.isdigit():
            digit_count += 1

    return [letter_count,digit_count]

sentence="Infosys 123"
print(count_digits_letters(sentence))
