# JSON Handling with Python

Python provides built-in support for JSON through the `json` module.

## Importing the JSON Module

To work with JSON in Python, you need to import the `json` module:

```python
import json
```

## Parsing JSON

To parse a JSON string and convert it into a Python dictionary, you can use the `json.loads()` method:

```python
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)
# Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

## Reading JSON from a File

To read JSON data from a file and convert it into a Python dictionary, use the `json.load()` method:

```python
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
```

## Writing JSON to a File

To write a Python dictionary to a file in JSON format, use the `json.dump()` method:

```python
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w') as file:
    json.dump(data, file)
```

## Converting Python Objects to JSON

To convert a Python dictionary to a JSON string, use the `json.dumps()` method:

```python
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)
# Output: {"name": "John", "age": 30, "city": "New York"}
```

## Pretty Printing JSON

To print JSON data in a more readable format, you can use the `indent` parameter with `json.dumps()`:

```python
json_string = json.dumps(data, indent=4)
print(json_string)
```

This will output the JSON string with an indentation of 4 spaces.

## Conversion table

json conversion and parsing is done using following table

| JSON           | Python |
|----------------|--------|
| object         | dict   |
| array          | list   |
| string         | str    |
| number (int)   | int    |
| number (real)  | float  |
| TRUE           | True   |
| FALSE          | False  |
| null           | None   |

## Conclusion

Python's `json` module makes it easy to parse JSON strings, read and write JSON files, and convert Python objects to JSON and vice versa. This is particularly useful for web applications and APIs that commonly use JSON for data exchange.
For further detail refer this document [https://docs.python.org/3.12/library/json.html](https://docs.python.org/3.12/library/json.html)
