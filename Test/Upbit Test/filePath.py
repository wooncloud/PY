import os

#os.chdir("/.key")
path = os.getcwd() + "/.key/slackToken.txt"

f = open(path, 'r')
while True:
    line = f.readline()
    if not line: 
        break
    print(line)
f.close()