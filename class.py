from numpy import average


class Student:
    def __init__(self,name,age,toan,van,teacher):
        self.name = name
        self.age = age
        self.toan = toan
        self.van = van
        self.teacher = teacher
        
    def average_score(self):
        ave_score = (self.toan + self.van)/2
        return ave_score

    def print_info(self):
        ave = str(self.average_score())
        print("Student name " + self.name + " study with " + self.teacher + " have average score " + ave)
student = []

s1 = Student("Cường", 21, 9, 10, "Dũng Lại")
s2 = Student("Trinh", 20, 10, 10, "Dũng Lại")
s3 = Student("Chinh", 21, 8, 9, "Dũng Lại")

s2.teacher = "Jane"

student.append(s1)
student.append(s2)
student.append(s3)

for i in range(len(student)):
    student[i].print_info()
