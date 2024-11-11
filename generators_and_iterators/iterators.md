# Iterators in Python

An object representing a stream of data. Repeated calls to the iterator’s `__next__()` method (or passing it to the built-in function `next()`) return successive items in the stream. When no more data are available a `StopIteration` exception is raised instead. At this point, the iterator object is exhausted and any further calls to its `__next__()` method just raise `StopIteration` again. Iterators are required to have an `__iter__()` method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a `list`) produces a fresh new iterator each time you pass it to the `iter()` function or use it in a `for` loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.

## Example

Here is a simple example of an iterator in Python:

```python
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration

# Usage
my_iter = MyIterator(1, 5)
for num in my_iter:
    print(num)
```

In this example:
- The `MyIterator` class implements the iterator protocol with the `__iter__()` and `__next__()` methods.
- The `__iter__()` method returns the iterator object itself.
- The `__next__()` method returns the next value and raises `StopIteration` when there are no more values to return.
- The `for` loop is used to iterate over the `MyIterator` object, printing numbers from 1 to 4.
