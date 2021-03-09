def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    # I was going to approach this with regex or splitting, at least for a naive approach, but then found a native method:
    return phrase.capitalize()

    # SF Alternate solution, using slicing:
    # return phrase[:1].upper() + phrase[1:]
