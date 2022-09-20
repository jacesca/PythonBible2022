# This program called Travis is going to have a
# list of known users, and every time it runs,
# it is going to ask for your name. If you are in
# the list of known users, it will welcome you and
# ask if you want to be removed from the list.
# If it does not recognize you, it will ask if you
# would like to be added to the list.

known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred',
               'Georgie', 'Harry']
YN_message = 'Only Y or N are valid answers. Please, try it again...'
affirmative_greetings = 'Have a nice day and see you soon!'

while True:
    print('\n\nHi! My name is Travis')
    while True:
        name = input('What is your name? (q to quit):').strip().title()
        if name != '': break

    if name == 'Q':
        break
    elif name in known_users:
        print('Hi {}! I see you are in the system.'.format(name))
        while True:
            answer = input('Would you like to be removed? (Y/N):').strip().upper()
            if answer == 'Y':
                known_users.remove(name)
                print('Removed! {}'.format(affirmative_greetings))
                break
            elif answer == 'N':
                print("No problem, I didn't want you to leave anyway. See you soon!")
                break
            else:
                print(YN_message)
    else:
        print("Hmmm I don't think I have met you yet {}...".format(name))
        while True:
            answer = input('Would you like to be added to the system? (Y/N):').strip().upper()
            if answer == 'Y':
                known_users.append(name)
                print('Added! {}'.format(affirmative_greetings))
                break
            elif answer == 'N':
                print('No worries, see you around!')
                break
            else:
                print(YN_message)
