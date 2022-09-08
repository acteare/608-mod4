# 608-mod4
## 5.1 - Introduction
- Collections: Prepackaged data structures consisting of related data items. (Ex: Contact lists, stocks in an investment portfolio)
- Dynamically Resize: Growing and shrinking at execution time. 

## 5.2 - Lists (see 5.2 examples in Chapter_5_Practice file)
- Homogenous Data: Values of the same data type
- Heterogeneous Data: Data of many different types.
#### You reference a list element by writing the list's name followed by the element's index enclosed in square brackets. 
- Index: The position number
#### Lists can also be accessed from the end by using negative numbers. 
- Note that when accessing from the end, the last number would be referenced with -1, not 0 or -0. 
#### Lists can be both mutable and immutable
- Mutable: Can be modified
- Immutable: Cannot be modified
    - Python's strings and tuple sequences are immutable
#### Concatenating Lists with +
- Concatenate: Combining two items one right after the other

## 5.3 Tuples (see 5.3 example in Chapter_5_Practice file)
- When you output a tuple, python always displays its contents in parentheses. 

## 5.4 - Unpacking Sequences (see 5.4 examples in Chapter_5_Practice file)
- You can unpack any sequences elements by assigning the sequence to a comma-separated list of variables. 
- Enumerate: This function receives an iterable and creates an interator that, for each element, returns a tuple containg the element's index and value.

## 5.5 - Sequence Slicing (see 5.5 examples in Chapter_5_Practice file)
- Slice: Creates new sequences of the same type containing subsets of the original elements. 
    - Slice operations can modify mutable sequences.

## 5.6 - del Statement (see 5.6 examples in Chapter_5_Practice file)
- del statement: Used to remove elements from a list and to delete variables from he interactice session.
    - You can remove the element at any valide index or the element(s)j from any valid slice. 

## 5.7 - Passing Lists to Functions (see 5.7 examples in Chapter_5_Practice file)
- Function 'modify_elements'items parameter receives a reference to the original lise, so the statement in the loop's suite modifies each element in the original list object. 

## 5.8 - Sorting Lists (see 5.8 examples in Chapter_5_Practice file)
- Sorting: Enables you to arrange data either in ascending or descending order. 
- Sort: This method modifies a list to arrange its elements in ascending order
- Reverse: this list method modifies a list to arrange its elements in descending order
    - Must be set to true in code Ex: numbers.sort(reverse=True)
- Sorted: This built in function returns a new list containing the sorted elements of its argument sequence -- the original sequence is unmodified. 

## 5.9 - Searching Sequences (see 5.9 examples in Chapter_5_Practice file)
- Searching: The process of locating a key value. 
- List Method Index: this takes as an argument a search key -- the value to locate in the list -- then seraches through the list from index 0 and returns the index of the first element that matches the search key

## 5.10 - Other List Methods
- insert: adds a new item at a specified index
- append: Add a new item to the end of a list
- extend: Add all the elemtns of another sequence to the end of a list
- remove: deletes the first element with a specified value
    - a ValueError will occur if the argument is not in the list
- clear: deletes all the elemtns in a list
- count: searches for its argument and returns the number of times it is found
- reverse: reverses the contents of a list in place, rather than creating a reversed copy

## 5.12 - List COmprehensions (see 5.12 examples in Chapter_5_Practice file)
- List comprehensions: a concise and convenient notation for creating new lists. 
    - These can replace many for statement that iterate over existing sequences and create new lists.

## 5.13 - Generator Expressions
- Generator Expressions: creates an iterable generator object that produces values on depend. 
- Greedy Evaluation: create lists immediately when you execute them. 

## 5.14 - Filter, Map and Reduce (see 5.14 examples in Chapter_5_Practice file)
- Higher-order Functions: functions that receive other functions as arguments
- lamnda expression (or lambda): used to define the function inline where it's needed -- typically as it's passed to another function.
    - begins with lambda keyword followed by a comma-separate parameter list, a colon (:) and an expression.

## 5.16 - Two-Dimensional Lists (see 5.16 examples in Chapter_5_Practice file)
- two-dimensional lists: Lists that require two indices to identify an element
- Multidimensional lists: Lists that require more than two indices to identify an element
- m-by-n list: A list with m rows and n columns

## 6.1 - Introduction
- Dictionary: an unordered collection which stores key-value pairs that map immutable keys to values, just as a conventional dictionary maps words to definitions
- Set: an unordered collection of unique immutable elements

## 6.2 - Dictionaries (see 6.2 examples in Chapter_6_Practice file)
#### A dictionary associates keys with values. Each key maps to a specific value. 
#### A dictionary's keys must be immutable (strings, numbers, tuples) and unique (no duplicates)
- Get: This method normally returns its argument's corresponding value. If that key is not found, get returns None.
- Dictionary Comprehensions: Provide a convenient notation for quickly generating dictionaries, often by mapping one dictionary to another.

## 6.3 - Sets (see 6.3 examples in Chapter_6_Practice file)
- Duplicate elimination: An automatic thing when creating a set. Removes any duplicate items in the set. 
    - The sets values are not displayed in the same order as they were listed in the original. 
    - Do not write code that depends on the order of their elements. 
- frozenset: an immutable set -- it cannot be modified after you create it, so a set can contain frozensets as elementns.
- issubset: Checks for an improper subset
- union: a set consisting of all the unique elements from both sets
- intersection: a set consisting of all the unique elements that the two sets have in common
- difference: a set consistion of the elements in the left operand that are not in the right operand
- symmetric difference: a set consisting fo the elements of both sets that are not in common with one another
- disjoint: is true if two sets do not have any common elements
