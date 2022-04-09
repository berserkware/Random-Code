class Human:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def sayname(self):
        print(self.firstname + " " + self.lastname)
        
    def sayage(self):
        print(self.age)
        


Caleb = Human("Caleb", "Mckay", 12)
Caleb.sayname()
Caleb.sayage()