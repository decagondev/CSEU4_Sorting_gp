"""
Getting the time complexity of an iterative solution
- Compute the Big-O for each line in isolation.
- If something is in a loop, multiply it's Big-O by the loop for the total.
- If two things happen sequentially, add the Big-Os.
- Drop leading multiplicative constants from each Big-O.
- From all the Big-Os that are added, drop all but the biggest, dominating one.
"""

it = [2,3,5,6,7]
# O(1)

def constant_time(items):
    result = items[0] * items[4] #O(1)
    print(result) # O(1)
    # O(4) Constant time operation O(1)

constant_time(it)

# O(n)

def linear_time(items):
    for item in items: # O(n) * O(1)
        print(item) # O(1)
    for item in items: # O(n) * O(1)
        print(item) # O(1)

linear_time(it)

# O(n^2)
def quadratic_time(items):
    for item in items: # O(n) * O(n) = O(n^2)
        for item2 in items: # O(n) * O(1)
            print(item, ' ', item2) # O(1)

quadratic_time(it)

# challenge. What is the complexity of this algorithm?

def complex_algo(items):

    for _ in range(5):
        print ("Python is awesome")

    for item in items:
        print(item)

    for item in items:
        print(item)

    print("Big O")
    print("Big O")
    print("Big O")

complex_algo([4, 5, 6, 8])