def permute_a_palindrome(input):
    
    impares = 0
    for char in set(input):
    
        can = input.count(char)
        if can %2 != 0:
            impares += 1
            
    if impares <= 1:
        return True 
    else:
        return False
    