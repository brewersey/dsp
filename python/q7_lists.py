# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.
    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    long_words = [lw for lw in words if len(lw) >= 2]
    count = 0
    i = 0
    while i < len(long_words):
        l = long_words[i]
        l = [w for w in l]
        if l[0] == l[-1]:
            count += 1
        i += 1
    return count

words = ['aaa', 'be', 'abc', 'hello']
matched = match_ends(words)
print(matched) 

def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    words = sorted(words, key = lambda x: (x[:][0] != 'x', x))
    return words

words = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
words = front_x(words)
print(words)
   

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    tuples = sorted(tuples, key = lambda x: x[-1])
    return tuples

tuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
tuples = sort_last(tuples)
print(tuples)

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.
    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    new_list = []
    new_list.append(nums[0])
    i = 0
    j = 1
    while j < len(nums):
        if new_list[i] != nums[j]:
            new_list.append(nums[j])
            i += 1
        j += 1
        
    return new_list

nums = [3, 2, 3, 3, 3]
nums = remove_adjacent(nums)
print(nums)

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.
    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    new_list = sorted(list1 + list2)
    return new_list

list1 = ['aa', 'xx']
list2 = ['bb', 'cc', 'zz']
new_list = linear_merge(list1, list2)
print(new_list)
