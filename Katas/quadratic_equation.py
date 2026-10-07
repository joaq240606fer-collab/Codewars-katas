def roots(a,b,c):
    discriminante = b**2 -4 *a *c    
    
    if discriminante >= 0:
    
        suma = -b/a
        
        return round(suma , 2)
    
    else:
        return None