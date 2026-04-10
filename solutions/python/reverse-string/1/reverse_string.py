def reverse(text):
    reversed_text=""
    text = list(text)
    for i in range(len(text)):
        lettre = text.pop(-1)
        reversed_text += lettre
    return reversed_text
