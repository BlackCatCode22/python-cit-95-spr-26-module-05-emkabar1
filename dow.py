fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

days = dict()
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    day = words[2]
    days[day] = days.get(day, 0) + 1

print(days)
