def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # Python has a `title()` methods for string
    return phrase.title()

    # SB Alternative approach
    # return ' '.join([s.capitalize() for s in phrase.split(' ')])

