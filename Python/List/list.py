import json
import os

listload = False

class List():
    def __init__(self, name):
        savedata = {}
        self.name = name
        self.savedata = savedata

    def save(self):
        with open(self.name + ".json", "w") as s:
            s.write(json.dumps(self.savedata))


    def load(self):
        with open(self.name + ".json") as l:
            self.savedata = json.load(l)

        

    def delete(self):
        pass
     
    def additem(self, item):
         pass

    def deleteitem(self):
        pass

    def showlist(self):
        for i in len(self.savedata.keys()):
            print(i)




def Run():
    loadedlist = ""
    print("say help for a list of commands")
    command = input("Enter a command: ").lower()
    if command == "help":
        print("List of commands:")
        print("create, creates a list")
        print("delete, deletes a list")
        print("load, loads a list")
        print("additem, adds item to list")
        print("deleteitem, deletes item from list")
        print("showlist, shows the list")
        print("exit, exits the list")
        Run()
    elif command == "create":
        print("what would you like to name your list?")
        listname = input()
        loadedlist = List(listname)
        loadeslist.save()
        Run()
    elif command == "delete":
        print("what list would you like to delete?")
        listtodelete = input()
        os.remove(listtodelete + ".json")
        Run()
    elif command == "load":
        print("what list would to load?")
        listtoload = input()
        loadedlist = List(listtoload)
        loadedlist.load()
        listload = True
        Run()
    elif command == "additem":
        print("what item would you like to add?")
        itemtoadd = input()
    elif command == "deleteitem":
        Run()
    elif command == "showlist":
        loadedlist.showlist()
    elif command == "exit":
        print("exiting list")
        listload = False
        Run()
    else:
        print("that is not a valid command")
        Run()
Run()
