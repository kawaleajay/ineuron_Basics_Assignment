
                                      
                                      ASSINGMENT - 8



1. Is the Python Standard Library included with PyInputPlus?
ANS:-PyInputPlus is not a part of the Python Standard Library, so you must install it separately using Pip
     #!pip install pyinputplus




2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
ANS:-pypi is alias of PyInputPlus.
     The as pyip code in the import statement saves us from typing pyinputplus each time we want to call a PyInputPlus function.
     Instead we can use the shorter pyip name. 




3. How do you distinguish between inputInt() and inputFloat()?
ANS:-inputInt() : Accepts an integer value, and returns int value
     inputFloat() : Accepts integer/floating point value and returns float value
     Both takes additional parameters ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’  for bounds




4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
ANS:-In the inputint function we can set the min = 0 and max =99 to ensure user enters number between 0 and 99.




5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
ANS:-we can also use regular expressions to specify whether an input is allowed or not. The allowRegexes and blockRegexes 
     keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or 
     reject as valid input.




6. If a blank input is entered three times, what does inputStr(limit=3) do?
ANS:-it will throw RetryLimitException exception.




7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
ANS:-When you use limit keyword arguments and also pass a default keyword argument, the function returns the default value instead of raising an exception.

