#Promt the user to enter their details
name = input('Student Name: ')
idnum = input('ID Number: ')
course_sec = input('Course and Section: ')

#Assign a value of grades
grade1 = eval(input('1st Quarter Grade: '))
grade2 = eval(input('2nd Quarter Grade: '))
grade3 = eval(input('3rd Quarter Grade: '))
grade4 = eval(input('4th Quarter Grade: '))

#assign number of grades for average
numofgrades = 4

#compute ave grades
ave = grade1 + grade2 + grade3 + grade4 / numofgrades

print('Student Name:', name)
print('ID Number:', idnum)
print('Course and Section:', course_sec)
print('Your Average of Grades is', ave)






