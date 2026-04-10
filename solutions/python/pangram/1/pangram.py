def is_pangram(sentence):
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = list(alphabet)
    sentence = sentence.replace("_", "")
    sentence = sentence.replace(" ", "")
    if sentence == "":
        return False
    
    for i in sentence:
        if i in alphabet:
            i = i.lower()
            alphabet.remove(i)
            i = i.upper()
            alphabet.remove(i)
            
    if len(alphabet) == 0:
        return True 

    return False