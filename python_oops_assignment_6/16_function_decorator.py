def log_function_call(func):
    def wrapper():
        print(f"Function i being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello, world!")

say_hello()