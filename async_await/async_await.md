# Async and Await in Python

Python's `async` and `await` keywords are used to write asynchronous code. They allow you to define asynchronous functions and handle asynchronous operations more efficiently.

## Async Function

An async function is defined using the `async def` syntax. It returns a coroutine object which can be awaited.

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Running the async function
asyncio.run(say_hello())
```

## Await

The `await` keyword is used to pause the execution of the async function until the awaited coroutine is complete. It can only be used inside an async function.

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(2)
    print("End")

# Running the async function
asyncio.run(main())
```

## Example: Fetching Data Asynchronously

Here's an example of fetching data from multiple URLs asynchronously:

```python
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            'http://example.com',
            'http://example.org',
            'http://example.net'
        ]
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

# Running the async function
asyncio.run(main())
```

In this example, `aiohttp` is used to perform HTTP requests asynchronously. The `asyncio.gather` function is used to run multiple coroutines concurrently.

By using `async` and `await`, you can write code that is more efficient and easier to read when dealing with asynchronous operations.