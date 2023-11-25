class Student:
    school_name='MES KUTTIPPURAM'
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Harry",20)
print('student:',s1.name,s1.age)
print('school name:',Student.school_name)
s1.name='jessa'
s1.age=19
print('student:',s1.name,s1.age)
Student.school_name='MES school'
print('school name:',Student.school_name)
