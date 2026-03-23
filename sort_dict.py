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

# lst = list()
# for k, v in counts.items():
#     lst.append((v, k))
#
# lst.sort(reverse=True)

lst = sorted([ (v, k) for k, v in counts.items() ], reverse=True)

print('Top 5 words by frequency:')
for v, k in lst[:5]:
    print(k, v)
