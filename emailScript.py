import csv

def readCSV(source, index):
    l = []
    with open(source) as c:
        csv_reader = csv.reader(c, delimiter=',')
        for row in csv_reader:
            item = row[int(index)]
            if item.count('@') > 0:
                l.append(item.casefold())
    l.sort()
    return l

def processCSV():
    source = input('Drag the .csv email list into the terminal: ')
    index = input('What row number are the emails in (the uconntact roster holds them in 4)?: ')
    source = source.replace(' ', '')
    return readCSV(source, index)

def processSTR():
    s = input('Enter the string list (it will be split at commas): ')
    l = s.split(', ')
    for i in range(len(l)):
        item = l[i]
        if item.count('@') > 0:
            l[i] = l[i].casefold()
    return l

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

def run():
    input('Welcome to the email tool! (press anything to continue)')
    answer = ''
    while answer != 'p' and answer != 'u' and answer != 'e':
        answer = input('Would you like to print .csv file, or find the union of two email lists (p/u/e)?')
    if answer == 'p':
        s = ''
        l = readCSV(input('Drag .csv file into terminal: '), input('Number of row to be printed: '))
        for i in range(1, len(l)):
            s = s + ', ' + l[i]
        s = l[0] + s
        print(s)
    elif answer == 'u':
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
            again()
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
            again()
    else:
        send = ''
        while send != 'y' and send != 'n':
            send = input('Send Email? (y/n) ')
        if send == 'y':
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from secrets import email, password


            from_addr= email
            subject = input('subject: ')
            body = input('body: ')
            recipients = input('to (if all, "all"): ')
            if recipients == 'all':
                recipients = l
            else:
                recipients = recipients.split(',')

            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login(email, password)
            
            for to_addr in recipients:
                msg = MIMEMultipart()
                msg['From']=from_addr
                msg['To']=" ,".join(to_addr)
                msg['subject']= subject

                msg.attach(MIMEText(body,'plain'))

                text = msg.as_string()
                mail.sendmail(from_addr,to_addr,text)

            mail.quit()
            again()
def again():
    answer = ''
    while answer != 'y' and answer != 'n':
        answer = input('Sucess! Continue? (y/n): ')
    if answer == 'y':
        run()
run()
