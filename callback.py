import time

# By passing cb (callback) as a parameter, we can callback functions within functions. We can essentially reuse the main chunk of a function and then callback a new function. Asynchronous programming.
def greet(name, cb):
    print(f'Hello {name}!')
    # time.sleep(3)
    cb()

def say_bye():
    print('Bye!!')

def shout():
    for i in range(5):
        print('SHOUT')

# Main
greet('Tyson', say_bye)
greet('Mary', shout)

print('Continuing main...')
# More statements


