# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        return 'Number of donuts: {0:d}'.format(count)
    else:
        return 'Number of donuts: many'

number = 5
breakfast = donuts(number)
print(breakfast)


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    list_s = [l for l in s]
    if len(list_s) > 2:
        new_string = list_s[0] + list_s[1] + list_s[-2] + list_s[-1]
        new_string = ''.join(new_string)
    else:
        new_string = ''
    
    return new_string

word = 'spring'
new_word = both_ends(word)
print(new_word)


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    list_s = [l for l in s]
    count = 1
    while count < len(list_s):
        if list_s[count] == list_s[0]:
            list_s[count] = '*'
        count += 1
    new_string = ''.join(list_s)
    return new_string

fs = 'donut'
new_fs = fix_start(fs)
print(new_fs)


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    a_string = [l for l in a]
    b_string = [l for l in b]
    
    z = a_string[0]
    y = a_string[1]
    x = b_string[0]
    w = b_string[1]
    
    a_string[0] = x
    a_string[1] = w
    b_string[0] = z
    b_string[1] = y
    
    a = ''.join(a_string)
    b = ''.join(b_string)
    new_string = ' '.join([a, b])
    return new_string

first = 'mix'
second = 'pod'
new_string = mix_up(first, second)
print(new_string)
        

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    list_s = [l for l in s]
    if len(list_s) >= 3:
        test1 = list_s[-3:]
        test1 = ''.join(test1)
        if test1 == 'ing':
            list_s.append('ly')
        else:
            list_s.append('ing')
        new_string = ''.join(list_s)
        return new_string
    else:
        return s

verb = 'swiming'
new_string = verbing(verb)
print(new_string)
        
def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    list_s = s.split()
    knots = [k for k in enumerate(list_s) if k[1] == 'not']
    bads = [b for b in enumerate(list_s) if b[1] == 'bad']
    
    if len(bads) == 0:
        return s
    elif bads[0][0] > knots[0][0]:
        stop = knots[0][0]        
        new_string = list_s[:stop]
        new_string.append('good')
        new_string = ' '.join(new_string)
        return new_string
    else:
        return s
    
phrase = 'This bad tea is not hot'
new_phrase = not_bad(phrase)
print(new_phrase)      
    
def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
   
    list_a = [l for l in a] 
    list_b = [l for l in b]
    
    afront = len(list_a)//2 + len(list_a)%2
    aback = -(len(list_a) - afront) 
    
    bfront = len(list_b)//2 + len(list_b)%2
    bback = -(len(list_b) - bfront)   
    
    section_1 = list_a[:afront]
    section_1 = ''.join(section_1)
    
    section_2 = list_b[:bfront]
    section_2 = ''.join(section_2)
    
    section_3 = list_a[aback:]
    section_3 = ''.join(section_3)
    
    section_4 = list_b[bback:]
    section_4 = ''.join(section_4)
    
    new_string = section_1 + section_2 + section_3 +section_4
    return new_string

a = 'Kitten'
b = 'Donut'
c = front_back(a, b)
print(c)
