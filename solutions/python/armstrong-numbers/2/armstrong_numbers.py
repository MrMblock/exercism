def is_armstrong_number(number):
    if number == sum_number(number):
        return True
    return False

def sum_number(number):
    total = 0
    power = __get__length(number)
    for i in str(number):
        total += int(i) ** power
    return total
        
def __get__length(number):
    return len(list(str(number)))