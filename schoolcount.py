fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

domains = dict()
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    domain = email.split('@')[1]
    domains[domain] = domains.get(domain, 0) + 1

print(domains)
