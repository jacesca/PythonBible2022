def add(*numbers):
    return sum(numbers)

print(add(*[1,2,3]))
print(add(*[2]))
print(add(2))
print(add(2,3,4))


def foo(**d):
    for k, v in d.items():
        print(k,':',v)

foo(age=23, name='Bob')
