                         
                                   ASSINGMENT - 6



1. What are escape characters, and how do you use them?
ANS:-In Python strings, the backslash "\" is a special character, also called the "escape" character. 
     It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return

     prefixing a special character with "\" turns it into an ordinary character. 
     This is called "escaping". For example, "\'" is the single quote character. 'It\'s Sunday' therefore is a valid string and equivalent to "It's Sunday".
     Likewise, '"' can be escaped: "\"hello\"" is a string begins and ends with the literal double quote character. Finally, "\" can be used to escape itself: 
     "\\" is the literal backslash character.
#print("it's Sunday")
#above sentence can be reperesented using escape charecter as
#print('it\'s Sunday')
output:-
#it's Sunday
#its's Sunday



2. What do the escape characters n and t stand for?
ANS:-"\t" is a tab, "\n" is a newline



3. What is the way to include backslash characters in a string?
ANS:-print('its a back slash \\ in a sentence')
     print('its a back slash \\ in a sentence') # ans:-its a back slash \ in a sentence



4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the
word Howl's not escaped a problem?
ANS:-The single quote in Howl's is fine because you've used double quotes to mark the beginning and end of the string. 
     like wise we can use double quotes in with single quotes.
     # print("HowI's Moving Castle")
     #output:- HowI's Moving Castle
     # like wise we can use double quote in side single quote
     # print('Its a "Nice" Sunday')
     # output:-Its a "Nice" Sunday



5. How do you write a string of newlines if you don't want to use the n character?
ANS:-we can use the parameter end ='\n' in print function.

     # print("printing something in multiple lines",end = '\n')
     # print("newline")
     # output:-
     # printing something in multiple lines
     # newline



6. What are the values of the given expressions?
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
ANS:- e
      Hello
      Hello
      lo, world



7. What are the values of the following expressions?
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
ANS:- 'HELLO'
       'True'
       'hello'



8. What are the values of the following expressions?
'Remember, remember, the fifth of July.'.split()
'-'.join('There can only one.'.split())
ANS:-'Remember, remember, the fifth of July.'.split() -> splits with space and returns list of words
      '-'.join('There can only one.'.split()) splits with space and join with '_'

    #   'Remember, remember, the fifth of July.'.split()
    #   output:-
    #   ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']

    #   '-'.join('There can only one.'.split())
    #   output:-'There-can-only-one.'



9. What are the methods for right-justifying, left-justifying, and centering a string?
ANS:-The following methods are used for justifying strings
     ljust()
     rjust()
     center()



10. What is the best way to remove whitespace characters from the start or end?
ANS:- lstrip() -> removes white spaces from left of the string
      rstrip() -> removes whitespaces from right of the string

