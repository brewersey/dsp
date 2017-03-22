import re
#collect degees
degrees = ['degree list']
with open('faculty.csv', 'r') as f:
    header = f.readline()
    header = header.split(',')
    #print(header)
    #for line in f:
    #    line = line.split(',')
        #print(line)
    
    for line in f:
        line = line.split(',')
        line = line[1]
        line = line.strip()
        line = line.split(' ')
        #print(line)
        degrees = degrees + line
#print(degrees)

#find unique degrees
unique = []
i = 0
j = 1
del degrees[0]
degrees.sort()
del degrees[0]

degrees = [x.replace('.', '') for x in degrees]
print(degrees)
print('\n')

unique = list(set(degrees))
unique.sort()
print(unique)
print(len(unique))

degree_number = {u: u for u in unique}
count = 0

for u in unique:
    with open('faculty.csv', 'r') as f:
        next(f)
        for line in f:
            line = line.replace('.', '')
            match = re.search(u, line)
            if match:
                count +=1
                degree_number[u] = count
    count = 0
                #print(match.group())
            #number.append(match.group())
print('\n')
print(degree_number)

#collect titles
titles = ['title list']
with open('faculty.csv', 'r') as f:
    header = f.readline()
    header = header.split(',')
    #print(header)
    #for line in f:
    #    line = line.split(',')
        #print(line)
    
    for line in f:
        line = line.split(',')
        line = line[2]
        #line = line.strip()
        #line = line.split(' ')
        #print(line)
        titles.append(line)
print(titles)

#find unique titles
unique = []
i = 0
j = 1
del titles[0]
titles.sort()
del titles[0]

titles = [x.replace(' of Biostatistics', '') for x in titles]
print(titles)
print('\n')

unique = list(set(titles))
unique.sort()
print(unique)
print(len(unique))

title_number = {u: u for u in unique}
count = 0

for u in unique:
    with open('faculty.csv', 'r') as f:
        next(f)
        for line in f:
            line = line.replace('.', '')
            match = re.search(u, line)
            if match:
                count +=1
                title_number[u] = count
    count = 0
                #print(match.group())
            #number.append(match.group())
print('\n')
print(title_number)

#collect degees
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
        line = line.split(' ')
        #print(line)
        emails.append(line)
print(emails)

domains = []

with open('faculty.csv', 'r') as f:
    #next(f)
    header = f.readline()
    header = header.split(',')
    #print('\n')
    #print(header)
    for line in f:
        line = line.split(',')
        line = line[3]
        line = line.replace('\n', '')
        #print(line)
        match = re.search(r'\@[\w.-]+', line)
        if match:
            domains.append(match.group())
#print(domains)
domains = [x.replace('@mail.', '') for x in domains]
print('\n')
#print(domains)

domains = [x.replace('@', '') for x in domains]
#print('\n')
#print(domains)  
unique_domains = set(domains)   
print(unique_domains)  
    
