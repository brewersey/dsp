# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> In python a list is a data strutuce that is composed of different data types seperated by comas and enclosed in square backets ` [] `.  In python a tuple is a data strutuce that is composed of different data types seperated by comas but are enclosed by parenthathese `()`.  The difference between a tuple and a list is that data in a tuple **cannot** be changed while data in a list can be.  Because of this tuples can be used as keys in dictionaries.  Like tuples dictionary key cannot be changed.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> As stated in question 1 In python a list is a data strutuce that is composed of different data types seperated by comas and enclosed in square backets ` [] `, but a set is a data strutuce that is composed of different data types seperated by comas and enclosed in curly backets `{}`.  The main differences between a set and a list are that set cannot contain duplicate entries whereas lists can.  Set aer also un-ordered data, consequently unlike list values in sets cannot be indexed; however, sets can be iterated through.  Python sets are designed to act like mathamatical sets whereas list are designed for the easy storage and accessing of data.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> In python a `lambda` is an ananonymous function, which means it is a user function that formally assinged to a variable, but it cannot be referenced beyond the first instance.  The syntax of lamdba functions follows: `lambda x: x - 2`.  In this case lambda created an instance of a function f(x) = x - 2.  Lambda functions are frequenty used in sorting commands to identify which element a list is to be sorted by.  For example if you had a list of tuple pairs ` pairs = [('apple', 'soot'), ('boy', 'sun'), ('cowboy', 'Sam'), ('door', 'Zor')]` and you wanted to sort them using sort `pairs.sort()` the resulting list will be sorted by the first element in the tuple; in this case the sorting will be don in alphabetical order.  If we wanted to sort by the second element we could use a `lambda` function as a key in the sort function, `pairs.sort(key=lambda pair: pair[1])`.  The list will now be sorted in alphabetical order (capital letters first!) based on the second element in the tuple.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is a tool in python that allows a programmer in one line to unpack and transform elements of a list into another list.  It follows the form `y = [f(x) for x in z if (condition)]`.  For examples if I had the list `singles = ['apple', 'boy', 'cowboy', 'door']` and wanted each element of the list to be in all caps we could use the list comprehension `upp = [x.upper() for x in singles]`.  In this example all of the words in list singles would be formatted to uppercase and transfered to the list `upp`.  If we wanted we could have incorporated if statement to specifiy which word we wanted in uppercase we could do so (ie `upp = [x.upper() for x in singles if x == 'door']` in this case `upp` only consists of `'DOOR'` since that was the only element of `singles` that meet the condition).

>> Essential a list comprehension is the combination of `python's` `map` and `filter` functions since:
>>`numbers = range(1, 11), squares = list(map(lambda x: x * x, numbers)), evens = list(filter(lambda x: x%2 == 0, squares))`
>>and
>>`numbers = range(1, 11), compeven = [x * x for x in numbers if (x * x)%2 == 0]`
>>produce the same results.  However, it is easier to manipulate strings using list comprehensions.

>>Set comprehensions and dictionary comprehensions also exist and follow the same structure:

>>Set: `single = set(['apple', 'boy', 'cowboy', 'door']), new_single = [x.upper() for x in single]`
Dictionay: `numbers = range(1, 11), squares = {x: x * x for x in numbers}`

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





