def guessGame():
    num = int(input())
    target = 6
    if num < target:
        print("your guess is almost there")
    elif num > target:
        print("your guess is higher")
    elif num == target:
        print("Your Guess Is Correct!")


# guessGame()
