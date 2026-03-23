fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

letters = dict()
for line in fhand:
    line = line.lower()
    for char in line:
        if char.isalpha():
            letters[char] = letters.get(char, 0) + 1

lst = sorted([(v, k) for k, v in letters.items()], reverse=True)

for count, letter in lst:
    print(letter, count)
