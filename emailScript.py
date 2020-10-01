import csv

#imnports csv and returns list
def readCSV(source, index):
    l = []
    with open(source) as c:
        csv_reader = csv.reader(c, delimiter=',')
        for row in csv_reader:
            item = row[int(index)]
            #if string has no @, it is not an email
            if item.count('@') > 0:
                l.append(item.casefold())
    l.sort()
    return l

#provides prompts for user
def processCSV():
    source = input('Drag the .csv email list into the terminal: ')
    index = input('What row number are the emails in (the uconntact roster holds them in 4)?: ')
    source = source.replace(' ', '')
    return readCSV(source, index)

#takes a string of emails and returns list of email strings
def processSTR():
    s = input('Enter the string list (it will be split at commas): ')
    l = s.split(', ')
    for i in range(len(l)):
        item = l[i]
        if item.count('@') > 0:
            l[i] = l[i].casefold()
    return l

#prompts differentiating string from csv
def question(time):
    if time == 1:
        answer1 = input('Is the first list a string or a .csv? (s/c): ')
    else:
        answer1 = input('Is the second list a string or a .csv? (s/c): ')
    if answer1 == 's':
        return processSTR()
    elif answer1 == 'c':
        return processCSV()
    else:
        return question(time)

#main loop
def run():
    input('Welcome to the email tool! (press anything to continue)')
    answer = ''
    while answer != 'p' and answer != 'u':
        answer = input('Would you like to print a .csv file, or find the union of two email lists (p/u)?')
    if answer == 'p':
        s = ''
        l = readCSV(input('Drag .csv file into terminal: '), input('Number of row to be printed: '))
        for i in range(1, len(l)):
            s = s + ', ' + l[i]
        s = l[0] + s
        print(s)
    else:
        l1 = question(1)
        l2 = question(2)
        l1 = set(l1)
        l2 = set(l2)
        l = list(l1.union(l2))
        s = ''
        for i in range(len(l) - 1):
            s = s + l[i] + ', '
        s = s + l[-1]
        a = 'w'
        while a != 'c' and a != 'p':
            a = input('Found ' + str(len(l)) + ' unique emails. Print or save as .csv? (p/c): ')
        if a == 'p':
            print('\nThe Combined List-\n' + s)
        else:
            fileName = input("Enter the filename for the .csv (don't include .csv): ")
            fileName = fileName + '.csv'
            directory = input('Drag folder for file into terminal: ')
            directory = directory.replace(' ', '')
            with open(directory + '/' + fileName, 'w') as newFile:
                writer = csv.writer(newFile)
                for i in l:
                    writer.writerow([i])
            input('File created. Thanks for using the email tool!')

run()
