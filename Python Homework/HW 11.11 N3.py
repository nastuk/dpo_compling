import random
allchoices = ""
password = ""
for x in range(4):
    allchoices = allchoices + random.choice('0123456789')
for x in range(3):
    allchoices = allchoices + random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')
for x in range(8):
    allchoices = allchoices + random.choice('qwertyuiopasdfghjklzxcvbnm')
for x in range(15):
    password = password + random.choice(allchoices)
print(password)
