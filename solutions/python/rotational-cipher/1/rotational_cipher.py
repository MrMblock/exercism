def rotate(text, key):
    alphabet_lower = list("abcdefghijklmnopqrstuvwxyz")
    alphabet_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    text = list(text)

    if key == 26:
        key = 0
    
    for i in range(len(text)):
       if text[i] in alphabet_lower or text[i] in alphabet_upper:
            if text[i].islower():
                new_index = alphabet_lower.index(text[i]) + key
                if new_index > 25:
                    new_index -= 26
                text[i] = alphabet_lower[new_index]
            elif text[i].isupper():
                new_index = alphabet_upper.index(text[i]) + key
                if new_index > 25:
                    new_index -= 26
                text[i] = alphabet_upper[new_index]

    return ''.join(text)        