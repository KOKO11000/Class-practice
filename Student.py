class Student:
    def __init__(self, name, grades = [int]):
        self.name = name
        self.grades = []
        
    def add_grade(self, grade):
        self.grades.append(grade)
        
        
        

    def average(self):
        sum_grades = sum(self.grades[:])
        average_grades = sum_grades / 2
        return f"total points: {sum_grades}, avrage points: {average_grades}"
    

student1 = (Student("Yuda", []))

student1.add_grade(95)
student1.add_grade(85)
student1.add_grade(75)
student1.add_grade(85)
student1.add_grade(90)
print(student1.grades)
print(student1.average())
