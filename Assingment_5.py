                         
                          ASSINGMENT - 5



1. What does an empty dictionary'S code look like?
ANS:- 
dict = {}
type(dict) #dict



2. What is the value of a dictionary value with the key 'foo' and the value 42?
ANS:-
{'foo':42}



3. What is the most significant distinction between a dictionary and a list?
ANS:- List - items in list are Ordered.
      Dictionary : iten in dictionary are unordered. 



4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
ANS:-This will give us KeyError
spam = {'bar':100}
spam['foo']  #its show error



5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
'cat' in spam.keys()?
ANS:-There is no differnce, both check if 'cat' is key of the dictionary and if its a key, returns True.
spam = {'cat':100}
'cat in spam'  # True

spam = {'cat':100}
'cat' in spam.leys() #True



6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
'cat' in spam.values()?
ANS:- 'cat' in spam checks whether there is a 'cat' key in the dictionary
      'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

spam = {'cat':100}
'cat'in spam  # True

spam = {'cat':100}
'cat' in spam.values() # False



7. What is a shortcut for the following code?

if 'color' not in spam:
spam['color'] = 'black'

ANS:-This can be achieved by using setdefault() which Inserts key with a value of default 
     if key is not in the dictionary.
spam = {'cat':100}
spam.setdefault('color','black')
print(spam)  #{'cat':100,'colo':'black'}



8. How do you "pretty print" dictionary values using which module and function?
ANS:-
import pprint

dct_arr = [ {'Name': 'John', 'Age': '23', 'Country': 'USA'},
  {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'},
  {'Name': 'Anne', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}
]  
pprint.pprint(dct_arr) #printing with pprint()

print(dct_arr)  #printing with print()




