# Get user email address
while True:
    email = input('What is your email?:').strip()
    if email != '': break

# Slice out user name
user = email[:email.index('@')]

# Slice domain name
domain = email[email.index('@')+1:]

# Format message
message = 'Your username is {} and your domain is {}'.format(user, domain)

# Display output message
print(message)
