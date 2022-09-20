# Ask user for name
while True:
    name = input('What is your name?:').strip()
    if name!='': break
    
# Ask user for age
while True:
    age = input('What is your age?:').strip()
    if age!='': break
    
# Ask user for city
while True:
    city = input('What city do you live in?:').strip()
    if city!='': break
    
# Ask user what they enjoy
while True:
    love = input('What do you love doing?:').strip()
    if love!='': break
    
# Create output text
message = """
Your name is {} and you are {} years old.
You live in {} and love {}.
"""
output_text = message.format(name, age, city, love)

# Print output to screen
print(output_text)
