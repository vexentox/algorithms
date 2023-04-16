import collections

def my_delete_nth(array, n): 
    counts, j = collections.defaultdict(int), 0
    for x in array:
        if counts[x] < n:
            array[j] = x
            j += 1
            counts[x] += 1
    del array[j:]
    return array[:j]

a = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(my_delete_nth(a, 2))

