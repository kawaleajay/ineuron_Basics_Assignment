                                
                                 ASSINGMENT - 4



1. What exactly is []?
ANS:-[] is a emplty list, like a =[]



2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)
ANS:-
# #SOLUTION BY CHANGING THE VALUE IN INDEX 3
spam = [2,4,6,8,10]
spam[2] = 'hello'
spam
# #SOLUTION BY INSERTING VALUE IN 3RD INDEX
spam = [2,4,6,8,10]
spam.insert(2,'hello')
spam



Let's pretend the spam includes the list ['a','b','c','d'] for the next three queries.

3. What is the value of spam[int(int('3' * 2) / 11)]?
ANS:-
spam = ['a','b','c','d']
spam[int(int('3' * 2)/11)]  #spam[int(33/11)] = spam[3]



4. What is the value of spam[-1]?
ANS:-
spam = ['a','b','c','d']
spam[-1] #NEGATIVE INDEX ANS: d



5. What is the value of spam[:2]?
ANS:-
spam = ['a','b','c','d']
spam[:2] #POSITIVE INDEX # ANS: 'a','b'



Let pretend bacon has the list [3.14, 'cat', 11,'cat', True] for the next three questions.

6. What is the value of bacon.index('cat')?
ANS:-
bacon = [3.14,'cat',11,'cat',True]
bacon.index('cat')   #IT RETURNS THE INDEX OF FIRST OCCURRENCE OF 'cat'



7. How does bacon.append(99) change the look of the list value in bacon?
ANS:-
bacon = [3.14,'cat',11,True]
bacon.append(99)
print(bacon)   #APPENDS ADDS THE ITEM AT THE END OF THE LIST.



8. How does bacon.remove('cat') change the look of the list in bacon?
ANS:-
bacon = [3.14,'cat',11,True]
bacon.remove('cat')
print(bacon)    # REMOVE FIRST OCCURRENCE OF ITEM


9. What are the list concatenation and list replication operators?

ANS:-Consider two lists:

a = [1,2,3]
b = [4,5,6]

If you need to concatenate them into a list, you could use the + operator. 
This will create a new list c:

c = a+b
print(c)  # ANS: [1,2,3,4,5,6]

If you need to replicate the list a say 3 times, you could use the * operator. 
This will create a new list d.

d = c*3
print(d)  # ANS:[1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]



10. What is difference between the list methods append() and insert()?
ANS:-The only difference between append() and insert() is that insert function allows us to 
     add a specific element at a specified index of the list unlike append() where we can add the element only at end of the list.__annotations.
      
bacon = [3.14,'cat',11,true]
bacon.append(88)
print(bacon) #append adds the item at the end of the list.

spam = [2,4,6,8,10]
spam.insert(2,'hello')
print(spam)  # solution by inserting value in 3rd index



11. What are the two methods for removing items from a list?
ANS:-remove(item) - removeds first occurence of a item.
     pop() - Remove and returns item at index (default last).
     del(list) - deletes the list.

bacon = [12,'dog',11,'cat',False]
bacon.ramove('dog')
print(bacon) #ANS: [12,11,'cat',False]

bacon = [3.14, 'cat', 11, 'cat', True]
bacon.pop()
print(bacon) # [3.14, 'cat', 11, 'cat']



12. Describe how list values and string values are identical.
ANS:-1. Both lists and strings can be passed to len()
     2. Have indexes and slices
     3. Can be used in for loops
     4. Can be concatenated or replicated
     5. Can be used with the in and not in operators.



13. What's the difference between tuples and lists?
ANS:-Lists :
     are mutable - they can have values added, removed, or changed. 
     lists use the square brackets, [ and ]
   Tuples :
     are immutable; they cannot be changed at all. 
    Tuples are written using parentheses, ( and ) while. 



14. How do you type a tuple value that only contains the integer 42?
ANS:-
tuple = (42)
print(tuple)  # (42)



15. How do you get a list value&'s tuple form? How do you get a tuple value's list form?
ANS:-
list_1 = [4,5]
l = tuple(list_1)
print(l)  # ANS: (4, 5)

tuple_1 = (5,6)
t = list(tuple_1)
print(tuple_1) # ANS: (5, 6)



16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they
contain?
ANS:- They contain references to list values.



17. How do you distinguish between copy.copy() and copy.deepcopy()?
ANS:-The copy.copy() function will do a shallow copy of a list, 
     The copy.deepcopy() function will do a deep copy of a list. 
     only copy.deepcopy() will duplicate any lists inside the 
     list.





    