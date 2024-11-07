# fizzbuzz

A simple python program for one of the MOST asked for interview questions for Junior developers. I added this so that if anyone is wondering, this is how to do it. 

We loop through a range of numbers (hard coded)
Along the way, if the number is divisible (using modulo division %) by 3 not 5, it prints Fizz,
if the number is divisible (using modulo division %) by 5 not 3, it prints Buzz,
and if the number is divisible (using modulo division %) by 3 AND 5, it prints FizzBuzz. 

Note ☝: 
The reason why we have if num % 3 == 0 and num % 5 == 0 evaluated at first is because if the number happened to be divisible at first by 3 or 5, 
whichever comparison comes first will be true and printed and the other comparisons will not happen. 
