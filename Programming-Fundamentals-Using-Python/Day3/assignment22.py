#PF-Assgn-22

def leap_year_check(year):
    if year % 400 == 0 or (year%4 == 0 and year%100 != 0):
        return True
    return False
    
def find_leap_years(given_year):
    list_of_leap_years = []
    while(len(list_of_leap_years) < 15):
        if leap_year_check(given_year):
            list_of_leap_years.append(given_year)
        given_year += 1
            
    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
