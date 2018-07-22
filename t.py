num = 3
if num > 0:
    print(num, "is a positive number")
    print("This is always printed")
    num = -1
    if num >0:
        print(num,"is a positive number")
        print("This is also always printed")

    parrot = "Norweign blue"
    letter = input(" Enter a character:")
    if letter in parrot:
        print("Give me an {}, Bob".format(letter))
    else:
     print("I dont need that letter")

     splitString = "This string has been\nsplit over\nseveral lines"
     print(splitString)
     tabbedstring = "1\t2\t3\t4\t5\t"
     print(tabbedstring)

     anotherSplitString = """This string has been
      split over
       several lines"""
     print(anotherSplitString)



