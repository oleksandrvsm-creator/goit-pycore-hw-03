from datetime import datetime
def get_days_from_today(date):
    try:
        new_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        difference = today - new_date

        return difference.days
    
    except ValueError:
        return 'You input incorrect format. Format must be: \'YYYY-MM-DD\''
    
print(get_days_from_today('2035-04-05'))

