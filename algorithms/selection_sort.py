def selection_sort(xs):
    pass

xs = [3,2,1,5,4]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check a list is sorted
# without replying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i+1] for i in range(len(xs)-1)))

# The all() function returns True if all items in an iterable are true, otherwise it returns False.