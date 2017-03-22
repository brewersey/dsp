emails = ['email list']
with open('faculty.csv', 'r') as f:
    header = f.readline()
    #header = header.split(',')
    #print(header)
    #for line in f:
        #line = line.split(',')
        #print(line)
        
    for line in f:
        line = line.split(',')
        line = line[3]
        line = line.replace('\n', '')
        #line = line.split(' ')
        #print(line)
        emails.append(line)
print(emails)

f = open('email_addresses.csv', 'a')
for address in emails:
    address = '\n' + address
    print(address)
    f.write(address)
f.close
