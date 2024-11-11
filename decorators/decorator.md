# Decorators in Python

A decorator in Python is a function that modifies the behavior of another function. Decorators allow you to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

## Example

Here is a simple example of a decorator:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### Explanation

1. `my_decorator` is a decorator function that takes another function `func` as an argument.
2. Inside `my_decorator`, there is a nested function `wrapper` that adds some behavior before and after calling `func`.
3. The `@my_decorator` syntax is a shorthand for `say_hello = my_decorator(say_hello)`.
4. When `say_hello()` is called, it actually calls the `wrapper` function, which adds the additional behavior.

Output:
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:

```python
@my_decorator
def say_hi():
    print("Hi!")
```

```python
def say_hi():
    print("Hi!")
say_hi = my_decorator(say_hi)
```

Decorators are a powerful tool in Python that can help you write cleaner and more maintainable code by separating concerns and promoting code reuse.