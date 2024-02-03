# Keygen

import random
from symbols import acceptChars, acceptLetters, acceptUpLetters


def main(n):
    keys = generate(n)
    
    with open('keygen/keys.txt', 'w') as file:
        for i in keys:
            file.write(i + '\n')
        
        
def generate(numberOfKeys):
    result = []
    key = ''
 
    for d in range(0,numberOfKeys):
        i = 0
        key = ''
        while i < 8:
            randomList = random.randint(0,2)
            
            if(randomList == 0):
                key += random.choice(acceptChars)
            elif(randomList == 1):
                key += random.choice(acceptLetters)
            else:
                key += random.choice(acceptUpLetters)
                
            i+=1
            
        result.append(key)
        
        
    return result

main(5)
    