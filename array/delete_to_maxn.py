import collections
def delete_to_maxn(array, n):
    """
    function：给定一个数组和一个数字 n ，创建一个新数组，其中每个数字至多 n 次而不重新排列。
    array : 数组状
    n : 每个数字至多重复 n 次
    return : 每个数字至多 n 次而不重新排列的数组
    """
    counts, j = collections.defaultdict(int), 0
    for x in array:
        if counts[x] < n:
            array[j] = x
            j += 1
            counts[x] += 1
    del array[j:]
    return array[:j]

a = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(delete_to_maxn(a, 2))
