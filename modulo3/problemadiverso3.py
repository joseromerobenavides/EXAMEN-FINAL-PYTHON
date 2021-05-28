from __future__ import division
 
def status(nota):
    if nota >=0 and nota < 4: return -1
    elif nota >= 4 and nota <=7: return 0
    elif nota > 7 and nota <= 10: return 1
    else: return None
 
    
 
