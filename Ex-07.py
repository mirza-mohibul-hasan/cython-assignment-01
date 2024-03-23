def fizzBuzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"


# print(fizzBuzz(3))
# print(fizzBuzz(15))
# print(fizzBuzz(5))
# print(fizzBuzz(7))
