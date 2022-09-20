# This system will offer a range of films, once the user pick
# the one he/she wants, the program will ask them for their age
# if they are old enough to watch the film and there are enough
# seats available then the program will let them use a book to
# see the film.
# If not the program will tell them that they're too young or
# there is no seats available.


films = {
    'Finding Dory': [3, 5],
    'Bourne': [18, 5],
    'Tarzan': [15, 5],
    'Ghost Busters': [12, 5]
}


while True:
    print('\n\nGood day, today we have the following films available: {}'.format(
        ', '.join(list(films.keys()))
    ))
    film_choice = input('Which film would you like to watch? (q to quit):').strip().title()
    if film_choice == 'Q':
        break;

    # Check if film is available
    elif film_choice in films:
        while True:
            age = input('How old are you?:').strip()
            if age.isdigit():
                # Check user age
                if int(age) >= films[film_choice][0]:

                    #Check enough seats
                    if films[film_choice][1]>0:
                        films[film_choice][1] -= 1
                        print('Here are your ticket, enjoy the film!')
                    else:
                        print('Sorry, we are sold out!')
                else:
                    print('You are too young to see that film!')
                break
    else:
        print('Oh! We do not have that film...')
