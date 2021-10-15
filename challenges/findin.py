class Challenge():
    def find(self, substring, string):
        listofwords = string.split(" ")

        newsubstring = substring.split(" ")
        

        for i in range(len(listofwords)):
            if listofwords[i] == newsubstring[0]:
                if len(newsubstring) > 1:
                    for x in range(len(newsubstring)):
                        if listofwords[i + 1] == newsubstring[x]:
                            return False
                        if x == (len(newsubstring) - 1):
                            return True
                else:
                    for i in listofwords:
                        if i == substring:
                            return True
                return False

    
    def count(self, substring, string):
        listofwords = string.split(" ")

        number = 0
        for i in listofwords:
            if i == substring:
                number += 1
        return number

app = Challenge()

string = "My name is Jess and this is lame"
print(app.find("is", string))# >> True
print(app.find("My name", string))# >> True
print(app.count("is", string))# >> 2
print(app.count("is lame", string))# >> 1
