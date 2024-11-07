
# FIZZBUZZ - yay!

# we are going to loop from numbers 1 to 100, and since 101 is not inclusive, we stop at 100
for num in range(1, 101):
    #This is important in our logic because if the number is divisible by both 3 and 5, we print Fizzbuzz. And operand
    #requires both conditions to be true.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        #if the number is divisible by just 5 not 2, print Buzz
    elif num % 5 == 0:
        print("Buzz")
        #if the number is divisible by just 3 not 5, print Fizz
    elif num % 3 == 0:
        print("Fizz")
        #otherwise (not divisible by either 3 or 5), just print the number
    else:
        print(num)

# The reason why we have if num % 3 == 0 and num % 5 == 0 evaluated at first is because if the number happened to be
# divisible at first by 3 or 5, whichever comparison comes first will be true and printed and the other comparisons
# will not happen.