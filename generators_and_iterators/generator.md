# Generators in Python

Generators are a simple way of creating iterators. They allow you to iterate through a sequence of values without storing the entire sequence in memory. Generators are written using functions and the `yield` statement.
Every generator is an iterator, but not vice versa. A generator is built by calling a function that has one or more `yield` expressions

## Example

Here is a simple example of a generator function:

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)
for number in counter:
    print(number)
```

In this example, the `count_up_to` function is a generator that yields numbers from 1 to `max`. Each call to `yield` produces a value and suspends the function’s state, allowing it to resume where it left off when the next value is requested.

## generator expression

An expression that returns an iterator. It looks like a normal expression followed by a for clause defining a loop variable, range, and an optional if clause. The combined expression generates values for an enclosing function

```python
# sum of squares 0, 1, 4, ... 81
sum(i*i for i in range(10))
# output of sum function is 285
```

## Benefits of Generators

- **Memory Efficiency**: Generators are memory efficient because they yield items one at a time and only when required.
- **Lazy Evaluation**: Generators use lazy evaluation, which means they generate items only when needed.
- **Readable Code**: Generators can make your code more readable and easier to understand.

Generators are a powerful tool in Python for handling large data sets and streams of data efficiently.

## How `yield` Works in Python

The `yield` statement is used in generator functions to produce a series of values. When a generator function calls `yield`, it produces a value and pauses its execution, saving its state. The next time the generator's `__next__()` method is called, the function resumes execution right after the `yield` statement, continuing until it hits another `yield` or returns.

Here is a step-by-step explanation of how `yield` works:

1. **Function Call**: When you call a generator function, it does not execute the function body immediately. Instead, it returns a generator object.
2. **First `yield`**: When you call `next()` on the generator object, the function starts executing until it hits the first `yield` statement. The value specified by `yield` is returned by the generator.
3. **State Suspension**: The function's state is saved, including local variables and the point of execution. This allows the function to resume where it left off.
4. **Subsequent `yield`**: Each subsequent call to `next()` resumes the function's execution from the last `yield` statement, runs until it hits the next `yield`, and returns the new value.
5. **Completion**: When the function runs out of values to yield (or explicitly returns), a `StopIteration` exception is raised, signaling that the generator is exhausted.

Example:

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
```

In this example, each call to `next(gen)` resumes the generator function from where it left off and continues until it hits the next `yield` statement.