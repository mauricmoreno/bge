def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

# Decorating the function
decorated_say_hello = my_decorator(say_hello)

# Calling the decorated function
decorated_say_hello()
