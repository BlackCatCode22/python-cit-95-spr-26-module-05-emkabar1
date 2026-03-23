fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

hours = dict()
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    time = words[5]
    hour = time.split(':')[0]
    hours[hour] = hours.get(hour, 0) + 1

lst = sorted([(hour, count) for hour, count in hours.items()])

for key, val in lst:
    print(key, val)
