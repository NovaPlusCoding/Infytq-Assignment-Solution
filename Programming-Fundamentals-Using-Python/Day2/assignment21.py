#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    _31days = [1,3,5,7,8,10,12]
    _30days = [4,6,9,11]
    
    if month in _31days and day == 31:
        next_day = 1
        next_month = month + 1
        if next_month > 12:
            next_month = 1
            next_year = year+1
        else:
            pass
       
    elif month in _30days and day == 30:
        next_day = 1
        next_month = month + 1
        if next_month > 12:
            next_month = 1
            next_year = year+1
        else:
            pass
    elif month == 2 and day == 28:
        next_day = 1
        next_month = month+1
        next_year = year
    else:
        next_day=day+1
        next_month=month
        next_year=year
        
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(28,2,2011)
