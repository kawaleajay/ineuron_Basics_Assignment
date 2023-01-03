                        #   ASSINGMENT - 2


# 1.What are the two values of the Boolean data type? How do you write them?
# ans:-The two values of the Boolean data type are true and false.
#      They can be written as value of expressions that have yes or no answers.
    #  it is used to represent the truth values of the expressions. For example, 1== 0 is True whereas 2>3 is False



# 2. What are the three different types of Boolean operators?
# ans:- "AND","OR" And "NOT" it is the three diffrent type of boolean operators.


# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).
# ans:-



# 4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)



# 5. What are the six comparison operators?
# ans:-



# 6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.



# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')

# ans:-

# spam = 0
# if spam == 10:
#     print('eggs')
# if spam > 5:
#     print('bacon')
# else:
#     print('ham')
#     print('spam')
#     print('spam')



# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.
# ans:-
# spam=int(input())
# if spam==1:
#     print("hello")
# elif spam==2:             #Example - 1
#     print("Howdy")
# else:
#     print("Gretting!")

# spam=int(input())
# if spam==1:
#     print("hello")
# if spam==2:              #Example - 2
#     print("howdy")
# else:
#     print("grettings")




# 9.If your programme is stuck in an endless loop, what keys you’ll press?

# ans:- I will press ctrl+c.



# 10. How can you tell the difference between break and continue?
# ans:-  The diffrence between break and continue statment is used for immediate termination of loop.
#        The Break statement is used to exit from the loop constructs.
#        continue statement perform again and again whenever condition is true.



# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# ans:- in a for loop range function in Python takes 3 arguments and they are initial value, final value and increment value.
#       There  is a no diffrence between range.




# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.
# ans:-
# for i in range(1 , 11):
#     print(i)

a=1
while(True):
    if a<=10:
        print(a)
        a=a+1




# 13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?