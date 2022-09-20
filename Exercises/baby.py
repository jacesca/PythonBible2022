# Simulate a conversation with a 3 year old kid.
from random import choice

questions = [
    'Why is the sky blue?',
    'Why is there a face on the moon?',
    'Where are all the dinosaurous?'
]
answer = input(choice(questions)).strip().lower()

while answer!='just because':
    answer = input('Why?:').strip().lower()

print('Oh!... Okay')
