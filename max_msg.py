fname = input('Enter file name: ')
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

lst = sorted([(count, email) for email, count in emails.items()], reverse=True)

count, email = lst[0]
print(email, count)
