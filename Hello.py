print("hello world")
parrot="Norweign Blue"
print(parrot)
print(parrot[0])
print(parrot[1])
print(parrot[2])
print(parrot[-3])
print(parrot[0:13])
print(parrot[0:-6:3])
number="9,223,456,476,876,946,834"
print(number[1::4])
number="1, 2, 3, 4, 5, 6, 7, 8, 9"
print(number[0::3])
string1 = "hey "
string2 = "dude "
print(string1 + string2)
print("hello " * 5)
print("hello " *(5+4))
print("hello" *5 +"4")
today="friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")


if grade >= 65: # Condition
 print("Passing grade") # Clause
else:
 print("Failing grade")

 from urllib.request import urlopen
 import urllib.error
 import twurl
 import json
 import sqlite3
 import ssl

 TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
 conn = sqlite3.connect('spider.sqlite')
 cur = conn.cursor()
 cur.execute('''
 CREATE TABLE IF NOT EXISTS Twitter
 (name TEXT, retrieved INTEGER, friends INTEGER)''')
 # Ignore SSL certificate errors
 ctx = ssl.create_default_context()
 ctx.check_hostname = False
 ctx.verify_mode = ssl.CERT_NONE

 while True:
  acct = input('Enter a Twitter account, or quit: ')
 if (acct == 'quit'): break
 if (len(acct) < 1):
  cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
 try:
  acct = cur.fetchone()[0]
 except:
  print('No unretrieved Twitter accounts found')
 continue
 url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
 print('Retrieving', url)
 connection = urlopen(url, context=ctx)
 data = connection.read().decode()
 headers = dict(connection.getheaders())
 print('Remaining', headers['x-rate-limit-remaining'])
 js = json.loads(data)
 # Debugging
 # print json.dumps(js, indent=4)
 cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct,))
 countnew = 0
 countold = 0
 for u in js['users']:
  friend = u['screen_name']
 print(friend)
 cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
             (friend,))
 try:
  count = cur.fetchone()[0]
 cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
             (count + 1, friend))
 countold = countold + 1
 except:
 cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
 VALUES (?, 0, 1)''', (friend,))
 countnew = countnew + 1
 print('New accounts=', countnew, ' revisited=', countold)
 conn.commit()
 cur.close()
 # Code: http://www.py4e.com/code3/twspider.py

 import socket

 mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 mysock.connect(('data.pr4e.org', 80))
 cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
 mysock.send(cmd)
 while True:
  data = mysock.recv(512)
 if len(data) < 1:
  break
 print(data.decode(), end='')
 mysock.close()