# Files and Exceptions

## What you will learn

Read/write files and handle errors.

## Example

```python
with open("data.txt", "w") as file:
    file.write("Hello")
```

```python
try:
    x = int("abc")
except:
    print("Error")
```

## Practice

* Write a file
* Handle errors

## Challenge

Save and load orders from a file.
