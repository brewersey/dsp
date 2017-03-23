#Question #6
directory = ['directory']
with open('faculty.csv', 'r') as f:
    header = f.readline()
    header = header.split(',')
    #print(header)
    for line in f:
        line = line.replace('\n', '')
        line = line.split(',')
        directory.append(line)
#print(directory)

faculty_list = []
count = 1
while count < len(directory):
    name = directory[count][0]
    name = name.split(' ')
    name = (name[-1])
    credential = directory[count][1:]
    entry = (name, credential)
    faculty_list.append(entry)
    count += 1

print('\n')
print(faculty_list)
print('\n')

#combine duplicates
last_names = [faculty_list[0]]
count = 0
i = 1
j = 0

while i < len(faculty_list):
    if  faculty_list[j][0] == faculty_list[i][0]:
        combined = faculty_list[j][1] + faculty_list[i][1]
        del last_names[-1]
        last_names.append((faculty_list[i][0], combined))
    else:
        last_names.append(faculty_list[i])

    j += 1
    i += 1

#print(last_names)

professor_dict = {k : v for k, v in last_names}
print(professor_dict)
print('\n')
count = 0
while count < 3:
    faculty = faculty_list[count][0]
    for key, value in professor_dict.items():
        if faculty == key:
            print(key, value)
    count += 1

    
#Question 7 & 8
directory = ['directory']
with open('faculty.csv', 'r') as f:
    header = f.readline()
    header = header.split(',')
    #print(header)
    for line in f:
        line = line.replace('\n', '')
        line = line.split(',')
        directory.append(line)
#print(directory)

faculty_list = []
count = 1
while count < len(directory):
    name = directory[count][0]
    name = name.split(' ')
    name = (name[0], name[-1])
    credential = directory[count][1:]
    entry = (name, credential)
    faculty_list.append(entry)
    count += 1

print('\n')
print(faculty_list)

professor_dict = {k : v for k, v in faculty_list}
print('\n')
count = 0
while count < 3:
    faculty = faculty_list[count][0]
    for key, value in professor_dict.items():
        if faculty == key:
            print(key, value)
    count += 1
    
#Question 8
#It appears that this code print out alphabetically by last name.  So sorting 
#to print by first name.

faculty_list_ln = sorted(faculty_list, key = lambda x: (x[:][0][0], x[:][0][1]))
print('\n')
count = 0
while count < 3:
    faculty = faculty_list_ln[count][0]
    for key, value in professor_dict.items():
        if faculty == key:
            print(key, value)
    count += 1

    
    
