from datetime import datetime


def get_days_from_today(date: str) -> str:
    '''calculation between 
    date and today'''
    try:
        new_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        difference = today - new_date

        return difference.days
    
    except ValueError:
        return 'You input incorrect format. Format must be: \'YYYY-MM-DD\''
    
if __name__ == "__main__":   
    print(get_days_from_today('2035-04-05'))

