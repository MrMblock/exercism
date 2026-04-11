def find_anagrams(word, candidates):
    anagrams = []
    for i in range(len(candidates)): 
        candidate = ''.join(candidates[i]).lower()
        word = word.lower()

        if candidate == word:
            continue
        elif sorted(candidate) == sorted(word):
            anagrams.append(candidates[i])
            
    return anagrams