# name = 'andy' # a comment
# print(f'hello {name}')

def greeting(name, surname=''):
    # this function returns a greeting message
    return f'hello {name} {surname}'

# print(greeting('ramon', 'geronimo'))
# print(greeting('alice', 'wonderland'))
# print(greeting('bob'))

greeting_ramon = greeting('ramon', 'geronimo')
# print(greeting_ramon)

# ...existing code...

def login(greeting_message):
    print(greeting_message)

login(greeting_ramon)
# ...existing code...
