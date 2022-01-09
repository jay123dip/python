num_of_student=int(input("Enter the number of students: "))
num_of_subjects=int(input("Enter the number of subjects: "))
for i in range(1,num_of_student+1):
    print('Student {}'.format(i))
    marks=0
    for j in range(1,num_of_subjects+1):
        j=int(input("Enter the subject marks {}:".format(j)))
        marks=marks+j;
    print('total marks {}'.format(marks))
    avg=marks/num_of_subjects
    print("average: {}".format(avg))
    if(avg >= 90):
        print("A Grade")
    elif(avg >= 80):
        print("B Grade")
    elif(avg >= 70):
        print("C Grade")
    elif(avg >= 60):
        print("D Grade")
    elif(avg >= 40):
        print("E Grade")
    else:
        print("Fail")

        