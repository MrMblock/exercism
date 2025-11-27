def response(hey_bob):
    greeting = "How are you?"
    
    if len(hey_bob.strip()) == 0:
        return "Fine. Be that way!"

    if hey_bob == greeting or hey_bob.strip()[-1] == '?' and hey_bob.isupper() == False:
        return "Sure."

    if hey_bob.isupper():
        if hey_bob[-1] == '?':
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"

    return "Whatever."

