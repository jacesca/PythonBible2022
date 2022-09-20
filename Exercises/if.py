x = 10
message = '{} is {} than {}!'

for i in range(3):
    while True:
        n = input('Please, write a number:').strip()
        if n.isdigit():
            n = int(n)
            break

    if n > x:
        print(message.format(n, 'bigger', x))
    elif x > n:
        print(message.format(x, 'bigger', n))
    else:
        print(message.format(n, 'equal', x))
