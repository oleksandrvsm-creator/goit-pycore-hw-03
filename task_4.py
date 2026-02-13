from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
  
    list_to_congratulate = []
    today = datetime.today().date()
    for user in users:

        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = user_birthday.replace(year=today.year)   
        birthday_next_year = user_birthday.replace(year=today.year + 1) 
        if birthday_this_year < today:
            congratulation_date = birthday_next_year
        else:
            congratulation_date = birthday_this_year
        if congratulation_date - today <= timedelta(days = 7): 
            
            if congratulation_date.weekday() >= 5:
                days_to_add = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days = days_to_add) 
            list_to_congratulate.append({'name': user['name'], 'congratulation_date': congratulation_date.strftime('%Y.%m.%d')})
        
    return list_to_congratulate    
            
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alex", "birthday": "1994.11.24"},
    {"name": "Ann", "birthday": "2006.02.20"},
    {"name": "Bill", "birthday": "1999.02.15"},
    {"name": "Den", "birthday": "1975.02.13"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)