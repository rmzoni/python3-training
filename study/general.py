import heapq

# Upacking for sums
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum([1, 2, 3]))

# Creating a priority queue
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)


# Creating a dict (map)
from collections import defaultdict
import json
d = defaultdict(list)
pairs = [(1, '1'), (2, '2')]
for key, value in pairs:
    d[key].append(value)
print(d)
print(json.dumps(d))

# Calculation with maps
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

prices_and_names = zip(prices.values(), prices.keys())
print(prices_and_names)

print(min(prices, key=lambda k: prices[k]))
print(prices[min(prices, key=lambda k: prices[k])])

# Finding Commonalities in Two Dictionaries
a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}

# Find keys in common
print(a.keys() & b.keys()) # { 'x', 'y' }
# Find keys in a that are not in b
print(a.keys() - b.keys()) # { 'z' }
# Find (key,value) pairs in common
print(a.items() & b.items()) # { ('y', 2) }

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)
# c is {'x': 1, 'y': 2}

# Removing Duplicates from a Sequence while Maintaining Order
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
set(a) # Does not preserve order
b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(b, key=lambda d: (d['x'],d['y']))))

# Naming a Slice
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])

# Determining the Most Frequently Occurring Items in a Sequence
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three) # Outputs [('eyes', 8), ('the', 5), ('look', 4)]
print(word_counts['not'])

# Sorting a List of Dictionaries by a Common Key
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]   

from operator import itemgetter
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

# Sorting Objects Without Native Comparison Support
from operator import attrgetter
#print(sorted(users, key=attrgetter('user_id')))

# Grouping Records Together Based on a Field
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Iterate in groups
from itertools import groupby
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# Filtering Sequence Elements
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

# Extracting a Subset of a Dictionary

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
print(p1)
# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }
print(p2)

# Mapping Names to Sequence Elements
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

# Transforming and Reducing Data at the Same Time
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)



def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found

def convertTabs(code, x):
    return code.replace('\t', ''.join([' ' for a in range(x)]))
