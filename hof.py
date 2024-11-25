# Higher-order functions
# Wrapper - it wraps the original function with some additional functionality

# In this program we are passing through our defined list into the function with_list and calling back either a squaring function or a cubing function to give us different results.

numbers = [5, 7, 2, 3]

# Builds a new list with the result of calling cb on each item on the list
# def with_list(nums, cb):
#     result = []
#     for n in nums:
#         result.append(cb(n)) # Double ** means 'to-the-power-of'

#     return result

def square(n):
    return n * n

def cube(n):
    return n **3

# Main
# print(with_list(numbers, cube))

# Same as above but using 'map', we have to cast map as type list in order to see the results. In a map's parameters, the function must be put first and then the iterable.
print(list(map(cube, numbers)))

# Unlike 'map', 'filter' returns a result if the function returns as 'True'. In the example below, only the number '2' in the list 'numbers' returns as True. 
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))
