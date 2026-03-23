import re

fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

data = fhand.read()

nums = re.findall('^New Revision: ([0-9]+)', data, re.MULTILINE)

int_nums = [int(n) for n in nums]
avg = sum(int_nums) / len(int_nums)

print(int(avg))
