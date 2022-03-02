fname = input('Input the file name: ')
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd")
else:
    try:
        fhand = open(fname)
    except:
        print('File could not be opened:', fname)
        quit()
    count = 0
    for line in fhand:
        if line.startswith('Subject: '):
            count = count + 1
    print('There were', count, 'subject lines in.', fname)
