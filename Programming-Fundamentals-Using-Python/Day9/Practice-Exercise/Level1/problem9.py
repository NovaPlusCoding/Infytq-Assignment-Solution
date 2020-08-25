#PF-Prac-9
def generate_dict(number):
    return {k:k*k for k in range(1,number+1)}
    
number=20
print(generate_dict(number))
