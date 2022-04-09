import random

def passwordgenerator():
    charecters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!", "@", "#", "$","%","^","&","*","(", ")", "_", "-", "+", "=", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" )
    password = ""
    for i in range(random.randrange(10, 20)):
        password += charecters[random.randrange(0, len(charecters))]

    return password

print(passwordgenerator())
