# Coroutine, `async` and `await`

In Python, coroutines are a special type of function that can pause and resume their execution. They are defined using the `async def` syntax and are used to write asynchronous code.

## Defining a Coroutine

To define a coroutine, use the `async def` syntax:

```python
async def my_coroutine():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
```

## Using `await`

The `await` keyword is used to pause the execution of a coroutine until the awaited coroutine completes. It can only be used inside an `async def` function.

Example:

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(2)
    print("End")

# Running the coroutine
asyncio.run(main())
```

In this example, `await asyncio.sleep(2)` pauses the execution of `main` for 2 seconds.

## Running Coroutines

To run a coroutine, you can use `asyncio.run()`:

```python
asyncio.run(my_coroutine())
```

Alternatively, you can use an event loop:

```python
loop = asyncio.get_event_loop()
loop.run_until_complete(my_coroutine())
loop.close()
```

## Summary

- Coroutines are defined with `async def`.
- Use `await` to pause coroutine execution.
- Run coroutines with `asyncio.run()` or an event loop.

Coroutines with `async` and `await` provide a powerful way to write asynchronous code in Python, making it easier to handle I/O-bound and high-level structured network code.

**`async` and `await` were intorduced in python 3.5**