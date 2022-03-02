fname = input('Enter the File Name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened')
    quit()

count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        spam = line[19:]
        fspam = float(spam)
        total = total + fspam
print('Average spam confidence', (total/count))
