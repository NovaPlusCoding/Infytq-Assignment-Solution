#PF-Prac-23
def divisible_by_sum(number):
    return number % sum(list(map(int,list(str(number)))))==0

number=42
print(divisible_by_sum(number))
