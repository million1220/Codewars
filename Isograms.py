def is_isogram(string):
    string = string.lower()
    char = []

    for i in string:
        if i in char:
            return False
        char.append(i)