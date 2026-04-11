def line_up(name, number):
    ext = "th"
    sentence = f"{name}, you are the {number}{ext} customer we serve today. Thank you!"

    end = ()
    if len(list(str(number))) >= 2:
        end = list(str(number))[-2], list(str(number))[-1]

    match end:
        case ("1", "1"):
            return sentence
        case ("1", "2"):
            return sentence
        case ("1", "3"):
            return sentence
            
    match list(str(number))[-1]:
        case "1":
            ext = "st"
        case "2":
            ext = "nd"
        case "3":
            ext = "rd"

    sentence = f"{name}, you are the {number}{ext} customer we serve today. Thank you!"
    return sentence
    