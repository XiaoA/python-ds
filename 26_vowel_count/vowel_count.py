VOWELS = set("aeiou")

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # This approach was close, but I should have instantiated a *SET* of VOWELS, instead of a list. Also, the solution puts the VOWELS constant in the global scope, which I probably would have done if I'd writen the method definition from scratch.
    # VOWELS = ["aeiou"]

    # phrase = phrase.lower()
    # counter = {}

    # for char in phrase:
    #     if char in VOWELS:
    #         counter[char] = counter.get(char, 0) + 1

    # return counter

    # SB Approach
    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1
            
    return counter
