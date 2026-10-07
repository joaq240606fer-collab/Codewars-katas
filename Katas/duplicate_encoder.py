def duplicate_encode(word):
    words = word.lower()
    result = ""
    for char in words:
        if words.count(char) >1:
            result += ")"
        else:
            result += "("
    return result