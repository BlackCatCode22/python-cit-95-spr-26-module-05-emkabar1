import string

fname = input('Enter file name: ')
if len(fname) < 1: fname = 'clown.txt'
fh = open(fname)

counts = dict()
for line in fh:
    line = line.lower().translate(line.maketrans("", "", string.punctuation))
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# print(counts)

bigcount = -1
bigword = None
for key, value in counts.items():
    # print(key, value)
    if value > bigcount:
        bigcount = value
        bigword = key

print('The most common word is:\n', bigword, '\nappearing', bigcount, 'times.')