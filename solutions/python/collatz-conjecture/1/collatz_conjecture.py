def steps(number):
    special_cases(number)
    total = 0
    while number != 1:
        if is_even(number):
            number = number / 2
            total += 1
        else:
            number = number * 3 + 1
            total += 1
    return total
            
def is_even(number):
    if number % 2 == 0:
        return True
    return False

def special_cases(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")