decimals = range (0,100)
my_range = decimals[3:40:3]
print(my_range == range (3,40,3))
print (range(0,5,2) == range (0,6,2))
print(list(range(0,5,2)))
print(list(range(0,6,2)))

r = range (0,100)
print(r)

for i in r [:: -2]:
    print(i)

    print ('='* 50)
    for i in range (99,0,-2):
        print(i)

        print("="* 50)
        print(range(0,100)[::-2] == range (999,0,-2))

        for i in range (0,100,-2):
            print(i)

            backString="egaugnal lufrewop yrev a si nohtyP"
            print(backString[:: -1])

            cast = ['Cleese', 'Idle', 'Gilliam', 'Jones', 'Palin', 'Chapman']

            print(cast.sort())

            for i in range (17):
                print("{0:>2} in hex is {0:>02x}" .format(i))

                x = 0x20
                y = 0x0a

                print(x)
                print(y)
                print(x*y)

                print(0b101010)

 powers = []
  for power in range(15,-1,-1):
    powers.append(2 ** power)

  print(powers)

 x = int (input("Please enter a number"))
  printing = False

for power in powers:
   bit = x // power
   if bit !=0 or power == 1:
    printing = True
   if printing:
       print(bit,end='')
   x %= power





