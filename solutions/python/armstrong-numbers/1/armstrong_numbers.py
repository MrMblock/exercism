def is_armstrong_number(number):
    length = __get__length(number)
    if number == sum_number(number):
        return True
    return False

def sum_number(number):
    sum = 0
    power = __get__length(number)
    for i in str(number):
        sum += int(i) ** power
    return sum
        
def __get__length(number):
    return len(list(str(number)))