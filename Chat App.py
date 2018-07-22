name = input ("Please enter your name:")
age = int (input ("How old are you, {0}? ".format(name)))
print(age)
if age >=18:
    print ("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years". format (18-age))

    print("Please guess a number line between 1 and 10:")
    guess = int (input())
    if guess <5:
        print ("Please guess higher")
        guess=int (input())
        if guess==5:
            print ("Well, done u guessed it")
        else:
            print("sorry u have not guesssed correctly")

            import textwrap

            string = "This is a very very very very very long string."
            print
            textwrap.fill(string, 8)