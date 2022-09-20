# Pig Latin is a simple joke language. It's imaginary
# that makes regular words hard to understand.
# Basically the way that it works is you take the first 
# consonant cluster of a word and you move those to the
# end, then you add the word 'yay'.

import re

def first_vowel(w):
    return re.search("[aeiou]", w, re.IGNORECASE)
    
def pig_translate(w):
    i = first_vowel(w)
    return (w if i is None else w[i.start():]+w[:i.start()])+('yay' if w[0] in 'aeiou' else 'ay')

while True:
    # get sentence from user
    sentence = input('Please, provide the sentence to translate (q to quit):').strip().lower()

    if sentence=='q':
        break
    elif sentence=='':
        pass
    else:
        # remove any special character
        sentence = re.sub('[^A-Za-z ]+', '', sentence)
        
        # split sentence into words
        # loop throught words and convert to pig latin
        # stick words back together
        # output the final string
        print('Tranlate:', ' '.join([pig_translate(word) for word in sentence.split(' ')]).capitalize())
        print('\n'*2)
