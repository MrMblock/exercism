def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    divisors = [] 
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    
    sum_perfect = 0
    for i in divisors:
        sum_perfect += i
    
    if number == sum_perfect:
        return "perfect"

    if number < sum_perfect:
        return "abundant"

    if number > sum_perfect:
        return "deficient"

    
    return False