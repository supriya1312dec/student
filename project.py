from statistics import mean as m

admin = {'python':'pass123@','user2':'pass2'}

studentDict = {'Jeff':[78,88,93],
               'alex':[92,76,88],
               'sam':[89,92,93]}

def enterGrades():
    nameToEnter = input('student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(ToEntergrade))
    else:
        print('Student does not exist.')

    print(StudentDict)

def removeStudent():
    nameToRemove= input('what student to remove?: ')
    if nameToRemove in studentDict:
        print('removing student...')
        del studentDict[nameToRemove]

    print(StudentDict)

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachstudent]
        avgGrade = m(gradeList)

    print(eachStudent,'has an average grade of:',avgGrade)

        
def main():
    print("""
Welcome to Grade Central
[1]- Enter Grades
[2]-Remove Student
[3]-Student Average Grades
[4]-Exit
""")
    action=input('What Would You Like to do today?(Enter a number)')
    if action=='1':
        print('1')
    elif action=='2':
        removestudent()
    elif action=='3':
        studentAVGs()
    elif action=='4':
        exit()
    else:
        print('No Valid Choice was given,try again')

login=input('username: ')
passw=input('password: ')

if login in admin:
    if admin[login] == passw:
        print('Welcome,',login)
        while True:
            main()
    else:
        print('Invalid password,will detonate in 5 seconds!')
else:
    print('Invalid username,calling the FBI to report this')
               
        
