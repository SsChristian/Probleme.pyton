class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}  # Initiaizam un dictionar pentru a stoca task urile
        Employee.empCount += 1

    def display_emp_count(self):
        """Displays the number of employees"""
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Tasks with status {status}:")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, departament):
        super().__init__(name, salary)  # Apelam constructoul clasei de baza
        self.departament = f"F01 {departament}"  # Adaugam departamentul
        Manager.mgr_count += 1  # Incrementam nr de manageri

    def display_employee(self):
        """Overrides the display_employee method to include department"""
        print(f"Department: {self.departament}")     #Name: {self.name}, Salary: {self.salary},


# Crearea instantelor pt manageri
mgr1 = Manager("Ioan Ionel", 35000, "IT")
mgr2 = Manager("Cristea Klementin", 28000, "HR")
mgr3 = Manager("Comsa Vlad", 10000, "Logistics")
mgr4 = Manager("Albu Radu", 7800, "Finance")





# Afisam managerii
print("\nManager 1:")
mgr1.display_employee()

print("\nManager 2:")
mgr2.display_employee()

print("\nManager 3:")
mgr3.display_employee()

print("\nManager 4:")
mgr4.display_employee()



# Afisam doar numele managerilor cu prefixul F01

print("\nNames of Managers:")
def display_names(*employees):
    """Afisam doar numele managerilor cu prefixul F01"""
    for emp in employees:
        if isinstance(emp, Manager):  # Verificam daca este manager
            print(emp.name)

display_names(mgr1, mgr2, mgr3, mgr4)

# Displaying counts

print("\nEmployee count:", Employee.empCount)
print("Manager count:", Manager.mgr_count)
