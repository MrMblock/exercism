def value(colors):
    values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    total = []
    
    for color in range(2):
        total.append(str(values[colors[color]]))

    return int("".join(total))