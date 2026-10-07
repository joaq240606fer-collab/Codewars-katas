def word_count(s):
    content = ["a", "the", "on", "at", "of", "upon", "in" , "as"]
    suma = 0
    
    limpia= ""
    
    for i in s :
        if i.isalpha():
            limpia += i
        else:
            limpia += " "
    
    words = limpia.split()
    
    for word in words:
        if word.lower() not in content:
            suma += 1
    return suma
