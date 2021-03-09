def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    # Initial pass
    # my_word = word.lower()
    # return my_word.count(letter.lower())

    
    # SB Solution
    return word.lower().count(letter.lower())
