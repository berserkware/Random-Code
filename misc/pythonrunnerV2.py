import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def find(filename, path):
    if filename.endswith(".py"):
        allfiles = find_all(filename, path)
        if len(allfiles) != 0:
            if(len(allfiles) > 1):
                for i in range(len(allfiles)) :
                    print(f"{i}: {allfiles[i]}")

                number = int(input("Number: "))
                try:
                    os.system(f"python {allfiles[number]}")
                except:
                    print("Invalid number")

            else:
                os.system(f"python {allfiles[0]}")
        else:
            print("There is no file with that name")
    else:
        print("That is not valid python file")

def run():
    while True:
        file = input("File -> ")
        driveletter = f"{input('Drive Letter ->')}:/"
        find(file, driveletter)


run()