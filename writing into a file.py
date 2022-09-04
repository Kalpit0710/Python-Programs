file=open("Student1.txt","w")
for i in range(5):
    name=input("Enter name of student:")
    file.write("Name of the student is : ")
    file.write(name)
    file.write('\n')
file.close()