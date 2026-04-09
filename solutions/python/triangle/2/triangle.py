def equilateral(sides):
    if is_inequal(sides):
        return False
    if is_same(sides):
        return True
    return False


def isosceles(sides):
    if is_inequal(sides):
        return False
    a, b, c = sides[0], sides[1], sides[2]
    if a == b or a == c or b == c and not is_same(sides):
        return True
    return False

def scalene(sides):
    if is_inequal(sides):
        return False
    a, b, c = sides[0], sides[1], sides[2]
    if a != b and b != c and c != a and not is_null(sides):
        return True
    return False

def is_null(sides):
    if sides == [0,0,0]:
        return True
    return False

def is_same(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if a == b and a == c and not is_null(sides): 
        return True
    return False

def is_inequal(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return True
    return False