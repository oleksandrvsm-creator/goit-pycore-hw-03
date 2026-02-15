import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> int:
    '''the function return 
    random numbers'''
    
    if  1 <= min <= max <= 1000 and 1 <= quantity <= (max - min):
        numbers = random.sample(range(min, max), k=quantity)
        return sorted(numbers)
    else:
        return []
    
if __name__ == "__main__":  
    lottery_numbers = get_numbers_ticket(10, 50, 4)
    print("Ваші лотерейні числа:", lottery_numbers)