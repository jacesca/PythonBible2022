# Getting deeper into strings
my_string = 'hello hello GREAT people'
print('Text            : ', my_string)
print('Length          : ', len(my_string))
print('Counting "l"    : ', my_string.count('l'))
print('Counting "k"    : ', my_string.count('k'))
print('Counting "hello": ', my_string.count('hello'))
print('Is lower?       : ', my_string.islower())
print('Is upper?       : ', my_string.isupper())
print('Is title?       : ', my_string.istitle())
print('Is alpha?       : ', my_string.isalpha()) #Because space is false
print('Is digit?       : ', my_string.isdigit())
print('Only A-Z0-9chars: ', my_string.isalnum()) #Because space is false
print('Upper           : ', my_string.upper())
print('Lower           : ', my_string.lower())
print('Capitalize      : ', my_string.capitalize())
print('Title           : ', my_string.title())
print('Index of e      : ', my_string.index('e'))
print('Find e          : ', my_string.find('e')) 
print('Index of people : ', my_string.index('people'))
print('Find people     : ', my_string.find('people')) 
try:
    print('Index of great  : ', my_string.index('great'))
except Exception as error_msg:
    print('Index of great  : ')
    print('"great" is not in the text!')
    print(type(error_msg))
    print(error_msg.args)
    print(error_msg)
print('Find great      : ', my_string.find('great'))
print('Find great      : ', my_string.lower().find('great'))
print('Strip hello     : ', my_string.strip('hello'))
print('Left strip hello: ', my_string.lstrip('hello'))
print('Rightstrip hello: ', my_string.rstrip('hello'))
print('Strip GREAT     : ', my_string.strip('GREAT'))
print('Slice 12-17     : ', my_string[12:18])
print('Slice with step2: ', my_string[::2])
print('Slice with step5: ', my_string[::5])
print('Slice step -1   : ', my_string[::-1])
print('Strip hello(rev): ', my_string[::-1].strip('hello'))
print('Slice step -2   : ', my_string[::-2])

text_to_find = 'GREAT'
print('Just a part     : ', my_string[my_string.index(text_to_find):])
