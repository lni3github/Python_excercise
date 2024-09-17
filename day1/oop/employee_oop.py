class Employee():
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

class Directory():
    def __init__(self):
        self.employees = {}

    def add(self, employee_obj):
        self.employees[employee_obj.employee_id] = employee_obj 

    def remove(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]

    def find_employee(self, employee_id):
        employee = self.employees.get(employee_id)
        if employee:
            return f"Name: {employee.name}, Department: {employee.department}"
        return "Employee not found"

employee1 = Employee("Deff", "T001", "DE1")
employee2 = Employee("Anna", "T002", "DE1")
employee3 = Employee("Jeff", "T003", "DE2")

directory = Directory()
directory.add(employee1)
directory.remove("T001")
print(directory.find_employee("T001"))