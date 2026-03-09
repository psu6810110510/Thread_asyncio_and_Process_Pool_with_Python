def FizzBuzz(X):
    if X % 3 == 0 and X % 5 == 0:
        return ("FizzBuzz")
    elif X % 3 == 0 :
        return ("Fizz")
    elif X % 5 == 0 :
        return ("Buzz")


#main 
FizzBuzz(5)