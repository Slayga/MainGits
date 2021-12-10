class Employee:
    def __init__(self, firstName, lastName, SSN):
        self.firstName = firstName
        self.lastName = lastName
        self.SSN = SSN

    def Information(self):
        return "Name: " + self.firstName, self.lastName, "Socialsecurity Number: " + self.SSN


class Teacher(Employee):
    def __init__(self, firstName, lastName, SSN, subjects):
        super().__init__(firstName, lastName, SSN)
        self.subjects = subjects


if __name__ == '__main__':
    test = Teacher("Gabriel", "Engberg", "0311", ["Eng", "Sve"])

    print(test.Information())
    print(test.subjects)