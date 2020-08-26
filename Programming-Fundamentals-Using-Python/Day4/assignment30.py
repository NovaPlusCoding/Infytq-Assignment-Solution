#PF-Assgn-30

def encode(message):
    count = 1
    message = message +'0'
    string = ""
    for i in range(len(message)-1):
        if message[i] == message[i+1]:
            count += 1
        else:
            string += str(count) + message[i]
            count = 1

    return string
    
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
