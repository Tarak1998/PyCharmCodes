    print("Please guess a number line between 1 and 10:")
   guess = int(input())
   if guess < 5:
    print("Please guess higher")
    guess = int (input())
   if guess == 5:
    print("Well done you guessed it")
     else:
    print ("Sorry you have not guessed correctly")
    elif guess > 5:
    print (" Please guess lower")
    guess = int(input())
     if guess == 5:
    print("Well, done u guessed it")
            else:
      print("Sorry u have not guesssed correctly")
      else:
       print ("You got it first time")