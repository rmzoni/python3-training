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