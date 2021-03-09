def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

    
    # Relevent Documentation:
    # https://docs.python.org/3/library/functions.html#open
    # https://docs.python.org/3/tutorial/inputoutput.html#tut-files
    # https://docs.python.org/3/library/stdtypes.html#bytearray.strip

    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(f"- {line}")
