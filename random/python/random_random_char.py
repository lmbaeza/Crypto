def random_char(from_value, to_value):
    char_from = ord(from_value)
    char_to = ord(to_value)
    return chr(random.randrange(char_from, char_to+1))