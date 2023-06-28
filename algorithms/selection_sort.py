def selection_sort(xs):
    for i in range(len(xs)-1):
        # Find minimum value in unsorted region.
        min_index = i
        for j in range(i+1,len(xs)):
            if xs[j] < xs[min_index]:
                min_index = j
        # after finding the minimum value in the unsorted region, swap with the first unsorted value.
        xs[i], xs[min_index] = xs[min_index], xs[i]


xs = [3,2,1,5,4]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check a list is sorted
# without replying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i+1] for i in range(len(xs)-1)))

# The all() function returns True if all items in an iterable are true, otherwise it returns False.