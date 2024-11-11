# A decorator is a function that expects ANOTHER function as parameter
def counter(a_function_to_decorate):
    # Inside, the decorator defines a function: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def wrapper(*args, **kwargs):
        # Put here the code you want to be executed BEFORE the original function is called
        print("Before the function runs")
        wrapper.count += 1
        print(f"Function {a_function_to_decorate.__name__} has been called {wrapper.count} times")

        # Call the function being decorated
        a_function_to_decorate(*args, **kwargs)

        # Put here the code you want to be executed AFTER the original function is called
        print("After the function runs")

    wrapper.count = 0

    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before and after. It’s ready to use!
    return wrapper

# @counter
def add(a, b):
    return a + b

print(add(1, 2))
print(add(2, 3))
print(add(3, 4))
print(add(4, 5))

# decorated_aad = counter(add)

# print(decorated_aad(1, 2))
# print(decorated_aad(2, 3))
# print(decorated_aad(3, 4))
# print(decorated_aad(4, 5))