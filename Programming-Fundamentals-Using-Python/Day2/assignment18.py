#PF-Tryout

def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    if current_currency_name == 'Euro':
        current_currency_amount = amount_needed_inr * 0.01417
    if current_currency_name == 'British Pound':
        current_currency_amount = amount_needed_inr * 0.0100
    if current_currency_name == 'Australian Dollar':
        current_currency_amount = amount_needed_inr * 0.02140
    if current_currency_name == 'Canadian Dollar':
        current_currency_amount = amount_needed_inr * 0.02027
    
    return current_currency_amount


#Provide different values for amount_needed_inr,current_currency_name and test your program
currency_needed=convert_currency(2000,"Euro")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
