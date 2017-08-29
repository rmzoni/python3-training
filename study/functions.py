# Writing Functions That Accept Any Number of Arguments
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))
# Sample use
print(avg(1, 2)) # 1.5
print(avg(1, 2, 3, 4)) # 2.5

# Writing Functions That Only Accept Keyword Arguments
def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(mininum(1, 5, 2, -5, 10)) # Returns -5
print(mininum(1, 5, 2, -5, 10, clip=0)) # Returns 0

# Attaching Informational Metadata to Function Arguments
def add(x:int, y:int) -> int:
    return x + y

print(add(1, 2))

# Returning Multiple Values from a Function
def myfun():
    return 1, 2, 3

# Defining Functions with Default Arguments
def spam(a, b=42):
    print(a, b)

# Defining Anonymous or Inline Functions
add = lambda x, y: x + y
print(add(2,3))
print(add('hello', 'world'))

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))

# Capturing Variables in Anonymous Functions
x = 10
a = lambda y: x + y
print(a(10))

# Replacing Single Method Classes with Functions
from urllib.request import urlopen
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

#yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
#for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
 #   print(line.decode('utf-8'))

# Carrying Extra State with Callback Functions
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)