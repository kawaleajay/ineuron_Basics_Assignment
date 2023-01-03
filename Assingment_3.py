                           ASSINGMENT - 3
            
    

1. Why are functions advantageous to have in your programs?
ans:-An advantage of using the functions is that coding time is reduced.
     And if you write the code again and again so you can call the functions.
     so you save the time of coding same routine multiple times.



2. When does the code in a function run: when it's specified or when it's called?
ans:-  The code in a function executes when the function is called, not when the function is defined.



3. What statement creates a function?
ans:-The def function Name() createes a function.



4. What is the difference between a function and a function call?
ans:- A function : is a block of code that does a particular operation and returns a result. It usually accepts inputs as 
      parameters and returns a result. 

      Function call : is the code used to pass control to a function



5. How many global scopes are there in a Python program? How many local scopes?
ans:-In a Python program, there is only one global scope,
     and a local scope is created whenever a function is called.



6. What happens to variables in a local scope when the function call returns?
ans:-When a function returns, the local scope is destroyed, and all the variables in it are forgotten.
     we will not be able to access the out side the function.



7. What is the concept of a return value? Is it possible to have a return value in an expression?
ans:-A return value is the value that a function call evaluates to.
     A return value can be used as part of an expression, Like any value



8. If a function does not have a return statement, what is the return value of a call to that function?
ans:-its return value is None,If there is no return statement for a function.



9. How do you make a function variable refer to the global variable?
ans:-By representing a valible by global keywaord in the body of a function.
     Example : global a



10. What is the data type of None?
ans:- NoneType is The data type of none.



11. What does the sentence import areallyourpetsnamederic do?
ans:-areallyourpetsnamederic ia not a python module. 
     Importing this module will throughs ModuleNotFoundError exception.



12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
ans:-This function can be called with spam.bacon(). like below
    import spam
    spam.bacon()



13. What can you do to save a programme from crashing if it encounters an error?
ans:-we can write lines of code in try block. This will not crash the programme. 
     And in except block we can catch the exception.



14. What is the purpose of the try clause? What is the purpose of the except clause?
ans:-Try : The code that could potentially cause an error goes in the try clause.
     except : The code that executes if an error happens goes in the except clause, like print statments about exceptions,
     loggin statements.