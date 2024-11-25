# By passing cb (callback) as a parameter, we can callback functions within functions. We can essentially reuse the main chunk of a function and then callback a new function. Asynchronous programming.
def greet(name, cb):
    print(f'Hello {name}!')
    cb()

# def say_bye():
#     print('Bye!!')

# Lambda is like saying 'def' in a new function
say_bye = lambda: print('Goodbye!!')

# Main
greet('Tyson', say_bye)

greet('Steve', lambda: print('Bye!'))

