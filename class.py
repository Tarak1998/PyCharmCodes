thisdict={"apple":"green",
"banana":"yellow", "cherry":"red"}

print(thisdict)

thisdict =	dict(apple="green", banana="yellow", cherry="red")
print(len(thisdict))

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


import time;

localtime = time.asctime( time.localtime(time.time()))
print  "Local current time : ", localtime


import calendar

# ask of month and year
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy,mm))

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0];
print "tup2[1:5]:   ", tup2[1:5];

import sqlite3
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.close()

name = "John Doe"
 greeting = "My name is {}".format(name)
 greeting
'My name is John Doe'
