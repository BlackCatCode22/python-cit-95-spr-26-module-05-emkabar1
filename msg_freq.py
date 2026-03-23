fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

emails = dict()
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    emails[email] = emails.get(email, 0) + 1

bigcount = -1
bigword = None
for key, value in emails.items():
    if value > bigcount:
        bigcount = value
        bigword = key

print(bigword, bigcount)
