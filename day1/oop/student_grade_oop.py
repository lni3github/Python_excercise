class Student():
    def __init__(self, name, grades:list):
        self.name = name
        self.grades = grades


class Classroom():
    def __init__(self):
        self.students = []

    def view_studens(self):
        for student in self.students:
            print(f"studentName: {student.name}, studentGrade: {student.grades}")

    def add(self, student_obj:Student):
        self.students.append(student_obj)
    
    def remove(self, student_name:str):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
    
    def average_grade(self, student_name:str):
        for student in self.students:
            if student.name == student_name:
                total_grade = 0
                total_num = 0
                for grade in student.grades:
                    total_num = (total_num) + 1
                    total_grade = total_grade + grade
                if total_num == 0:
                    return print("divided by zero")
                self.display_grade(int(total_grade/total_num))
    
    def display_grade(self, avg_grade:int):
        if avg_grade >= 80:
            print(f"{avg_grade} -> A")
        elif avg_grade <= 79 and avg_grade >= 75:
            print(f"{avg_grade} -> B+")
        elif avg_grade <= 74 and avg_grade >= 70:
            print(f"{avg_grade} -> B")
        elif avg_grade <= 69 and avg_grade >= 65:
            print(f"{avg_grade} -> C+")
        elif avg_grade <= 64 and avg_grade >= 60:
            print(f"{avg_grade} -> C")
        elif avg_grade <= 59 and avg_grade >= 55:
            print(f"{avg_grade} -> D+")
        elif avg_grade <= 54 and avg_grade >= 50:
            print(f"{avg_grade} -> D")
        else:
            print(f"{avg_grade} -> F") 

classroom = Classroom()
student1 = Student("Boss Navamin", [50,83,90,80,50,10])
student2 = Student("Jeff Deland", [20,30,10])
classroom.add(student1)
classroom.add(student2)
classroom.average_grade("Jeff Deland")
