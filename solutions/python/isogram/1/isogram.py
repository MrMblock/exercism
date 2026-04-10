def is_isogram(string):
    c = 0
    string = string.replace("-", "") 
    string = string.replace(" ", "")
    for i in string:
        for j in string:
            i = i.lower()
            j = j.lower()
            if i == j:
                c += 1
        if c > 1:
            return False
        c = 0
    return True