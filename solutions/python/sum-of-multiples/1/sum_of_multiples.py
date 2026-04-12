def sum_of_multiples(limit, multiples):
    list_multiples = []
    multiplier = 1
    
    for i in range(len(multiples)):
        while multiples[i] * multiplier < limit:
            if multiples[i] == 0:
                break
            if multiples[i] * multiplier not in list_multiples:
                list_multiples.append(multiples[i] * multiplier)
            multiplier += 1
        multiplier = 0
            
    sum_of_multiples = sum(list_multiples)
    return sum_of_multiples
