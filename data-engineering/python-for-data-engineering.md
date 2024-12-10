Reference:
- https://medium.com/@mariusz_kujawski/python-for-data-engineering-6bd6140033d4
- https://www.geeksforgeeks.org/literals-in-python/

# Build-in data structures
Python provides several built-in data structures that are widely used for various purposes. List, Tuple, Dictionary, and Set are four different types of data structures, each with its characteristics and use cases.

## List
Mutable: Lists are mutable, meaning you can modify their elements after the list is created. You can add, remove, or modify elements.

Syntax: Defined using square brackets [].

``` sh
my_list = [1, 2, 3, 'a', 'b', 'c']
my_list.append(4)     # Adds 4 to the end of the list
my_list.remove('a')  # Removes the element 'a'
```

## Tuple
Immutable: Tuples are immutable, meaning once they are created, their elements cannot be changed or modified. Unlike lists, you can’t add or remove elements from a tuple.

Syntax: Defined using parentheses ().

``` python
my_tuple = (1, 2, 3, 'a', 'b', 'c')
```

## Dictionary
Dictionaries are used to store data values in key-value pairs. A dictionary is a collection that is changeable and does not allow duplicates in the keys.

``` python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

## Set
Unordered and Unique Elements: Sets are unordered collections of unique elements. They do not allow duplicate values, and the order of elements is not guaranteed.

Syntax: Defined using curly braces {} or by using the set() constructor.

``` python
my_set = {1, 2, 3}
my_set.add(1)
my_set.add(1)
print(my_set)
## {1, 2, 3}
```

## Operations on Lists

### List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. This allows you to simplify code.

``` python
# Without list comprehension
squares = []
for i in range(5):
    squares.append(i**2)
print(squares)

# With list comprehension
squares = []
squares = [i**2 for i in range(5)]
print(squares)

# Output:
# [0, 1, 4, 9, 16]
```

### Filter, Map, and Reduce
Map, Filter, and Reduce allow the programmer to write simpler, shorter code, without loops.

#### Filter
Filter as the name suggests helps to filter your list using filter conditions.

``` python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Output: [2, 4, 6, 8]
```

#### Map
The Map function allows us to use a function on a list of elements.

``` python
def power2(val: int) -> int:
    return val*val

numbers = [1, 2, 3, 4, 5]

power_numbers = list(map(power2, numbers))
# OR
squared_numbers = list(map(lambda x: x**2, numbers))

# Output: [1, 4, 9, 16, 25]
```

#### Reduce

The reduce() function is a powerful tool in Python that operates on a list (or any iterable), applies a function to its elements, and ‘reduces’ them to a single output.

``` python
from functools import reduce

words = ["apple", "banana", "orange", "apple", "grape", "banana"]

# Count the occurrences of each word
word_counts = reduce(lambda counts, word: {**counts, word: counts.get(word, 0) + 1}, words, {})

print(word_counts)
# Output: {'apple': 2, 'banana': 2, 'orange': 1, 'grape': 1}


numbers = [1, 2, 3, 4, 5]
product = reduce((lambda x, y: x * y), numbers)

# Output: 120
```

### Enumerate
The enumerate function adds a counter to an iterable and returns it. If your background is in C# avoid using this:

``` python
lista = ['a','b','c','d','e']
count = 0
for l in lista:
    print('Index:', count,' Value:', l)
    count+=1
```

Use Enumerate to achieve the same result:
``` python
lista = ['a','b','c','d','e']
for count, l in enumerate(lista):
    print('Index:', count,' Value:', l)
```

### Generators
Python provides a generator to create your iterator function. A generator is a special type of function that does not return a single value, instead, it returns an iterator object with a sequence of values. In a generator function, a yield keyword is used instead of a return. It allows you to create an iterator without loading the entire dataset into memory, making it suitable for processing huge files.

``` python
text = """
transaction_id,user\r
1,aaa\r
\r
2,xx\r
3,ccc\r
\r
"""

def process_large_file(text):
        for line in text.split("\r"):
            # Process the line
            processed_line = line.strip().upper()

            if processed_line != "":
                # Yield the processed line
                yield processed_line

# Example usage

for processed_line in process_large_file(text):
    print(processed_line)

# Output:
# 1,AAA
# 2,XX
# 3,CCC
```
We can use it to adjust file format to remove content that doesn’t meet the CSV format requirements.

### Decorators
Python Decorators are used to apply additional functionality to objects. They are used to provide more functionality without having to write additional code inside the object. For example, we can modify the returned value and display it from the decorator function.

``` python
def make_upper(function):
 def upper():
  f = function()
  print(f"this from orgin value: {f}")
  return f.upper()
 return upper

@make_upper #decorator
def helloworld():
 return "hello world"

print(helloworld())

# Otput:
# this from orgin value: hello world
# HELLO WORLD
```

In practice, you can create a retry decorator to execute a function in the case of an error a few times.

``` python
import time

def retry(times, wait):

    def decorator(func):
        def newfn(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    time.sleep(wait)
                    return func(*args, **kwargs)
                except Exception as e:
                    print(
                        'Exception thrown when attempting to run %s, attempt '
                        '%d of %d' % (func, attempt, times)
                    )
                    attempt += 1
            time.sleep(wait)
            return func(*args, **kwargs)
        return newfn
    return decorator

@retry(times=3, wait=2)
def get_from_rest():
    print('Try read data from rest API')

    raise ConnectionError ('Lack of connection')

get_from_rest()
```

### Data Class
A data class in Python is a specially structured class that is optimized for the storage and representation of data. Data classes have certain built-in functions to take care of the representation of data as well as its storage.

Data class takes care of things like displaying values, and object comparison. We don’t need to use a constructor to assign values. You don’t need to implement __repr__, __eq__, or __hash__ for debugging and object comparison.

``` python
from dataclasses import dataclass


@dataclass #dataclass decorator
class cutomerD:
 name: str #Type Hints
 id: int
 surname: str

class customer:
 def __init__(self,name,aid,books):
  self.name = name
  self.id = aid
  self.surname = books

Obj1 = customer("Erick",1254,"Nowak")
Obj2 = customer("Erick",1254,"Nowak")

Obj3 = cutomerD("Erick",1254,"Nowak")
Obj4 = cutomerD("Erick",1254,"Nowak")


print("Difrence for debuging")
print(Obj1)
print(Obj3)

print("\nDifference in Equality Check")
print(Obj1==Obj2)
print(Obj3==Obj4)

# Output:
# Difrence for debuging
# <__main__.customer object at 0x0000021E1108AC80>
# cutomerD(name='Erick', id=1254, surname='Nowak')
#
# Difference in Equality Check
# False
# True

```

Easy way to convert to dictionary or tuple. It simplifies the code when we need to operate on this format and save data in JSON output.

``` python
from dataclasses import dataclass, astuple, asdict


@dataclass #dataclass decorator
class customer:
 name: str #Type Hints
 id: int
 surname: str


Obj1 = customer("Erick",1254,"Nowak")

print(astuple(Obj1))
print(asdict(Obj1))

# Output:
# ('Erick', 1254, 'Nowak')
# {'name': 'Erick', 'id': 1254, 'surname': 'Nowak'}

json.dumps(asdict(Obj1))
```

# Concurrency vs. parallelism
Concurrency and parallelism are names for two different mechanisms for task execution in a script. For a data engineer, these techniques will help to speed up the process of retrieving data from API or transforming data.

## Multithreading Pools
Multithreading is a way to achieve parallelism by executing multiple threads of code. A thread is a lightweight process that shares the same memory space as the parent process. To use multi-threading pools in Python, you can use the ThreadPoolExecutor class from the concurrent.futures module. Using threads we can parallel calls to API to retrieve data.

``` python
import calendar
from concurrent.futures import ThreadPoolExecutor
import requests

def generate_dates(year, month):
    _, last_day = calendar.monthrange(year, month)

    dates = [f"{year}-{month:02d}-{day:02d}" for day in range(1, last_day + 1)]
    return dates

year = 2023
month = 10
result = generate_dates(year, month)
urls = []
for x in result:
    urls.append(f"http://api.nbp.pl/api/exchangerates/rates/a/gbp/{x}/")

def download_page(url):
    response = requests.get(url)
    return response.content

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(download_page, urls))

for result in results:
    print(result)
```

## Multiprocessing Pools
Multiprocessing is a technique used to achieve parallelism by running multiple processes simultaneously. A process is an independent instance of a running program that possesses its own memory space. Python provides a built-in multiprocessing module that facilitates the creation and management of processes.

``` python
from multiprocessing import Pool
import time

def square(x):
    time.sleep(1)
    print(x)
    return x * 2


numbers = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    with Pool(processes=2) as pool:
        results = pool.map(square, numbers)
    print(results)
```

## Concurrency
Concurrency in Python can be achieved through coroutines or asynchronous programming, providing an alternative approach to running functions concurrently. Unlike traditional threading, coroutines use specific programming constructs and are managed by the Python runtime with significantly reduced overhead.

For example, consider the usage of asyncio:

``` python
import asyncio
import time

async def sql_command1():
    await asyncio.sleep(2)
    print("Query executed 1")
    return {"col1": 1, "col2": 2}


async def sql_command2():
    await asyncio.sleep(3)
    print("Query executed 2")
    return {"col1": 1, "col2": 2}

async def sql_command3():
    await asyncio.sleep(3)
    print("Query executed 3")
    return {"col1": 1, "col2": 2}


async def main():
    
 start_time = time.time()

 sql1 = asyncio.create_task(sql_command1())
 sql2 = asyncio.create_task(sql_command2())
 sql3 = asyncio.create_task(sql_command3())

 res1 = await sql1
 res2 = await sql2
 res3 = await sql3

 end_time = time.time()
 exec_time = end_time - start_time
 print(f"re1 {res1}")
 print(f"re2 {res2}")
 print(f"re3 {res3}")
 print(f"total time {exec_time:.2f}")

if __name__ == "__main__":
     asyncio.run(main())
```

Rather than executing code synchronously and waiting for each step, using this method allows us to import data simultaneously from different URLs, thereby reducing import time.

For example, here is an illustration of importing data from multiple URLs:

``` python
import aiohttp
import asyncio
import calendar

def generate_dates(year, month):
    _, last_day = calendar.monthrange(year, month)

    dates = [f"{year}-{month:02d}-{day:02d}" for day in range(1, last_day + 1)]
    return dates

year = 2023
month = 10
result = generate_dates(year, month)
urls = []
for x in result:
    urls.append(f"http://api.nbp.pl/api/exchangerates/rates/a/gbp/{x}/")

async def download_page(session, url):
    async with session.get(url) as r:
        return await r.text()


async def main():
    async with aiohttp.ClientSession() as session:
        datas = await asyncio.gather(*[download_page(session, u) for u in urls])
        for x in datas:
            print(x)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
```