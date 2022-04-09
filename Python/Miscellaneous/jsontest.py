import json

class Human():
    def __init__(self, age, firstname, lastname):
        self.age = age
        self.firstname = firstname
        self.lastname = lastname

    def ShowData(self):
        print("Age: " + str(self.age))
        print("First Name: " + self.firstname)
        print("Last Name: " + self.lastname)

    def save(self, savefilename):
        data = {
            "age" : self.age,
            "firstname" : self.firstname,
            "lastname" : self.lastname
        }
        with open(savefilename, 'w') as f:
            f.write(json.dumps(data))

    def Load(self, savefilename):
        with open(savefilename, 'r') as f:
            savedata = json.load(f)

        self.age = savedata["age"]
        self.firstname = savedata["firstname"]
        self.lastname = savedata["lastname"]

        

human1 = Human(46, "joe", "doe")
human1.Load("Caleb.json")
human1.ShowData()
