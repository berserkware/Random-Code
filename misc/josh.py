#Importing time module
import time

print("WELCOME TO THE COFFEE SHOP")
print('''\

                        (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \""--..__                              __..--""/
       '._     """----.....______.....----"""     _.'
          `""--..,,_____            _____,,..--""`
                        `"""----"""`
    ''')


t = 5 #10 seconds
print("Thank you so much for coming in today! \n")
name = input("What is your name? \n")
print(f"Hi {name}, \n This is the menu for today... \n")
print("Cappuccino \n Latte \n Espresso \n Flat White \n")
coffee = input("What would you like? \n")
print(f"Your {coffee} will be ready soon! \n")
time.sleep(t)
print(f"Here is your {coffee}, {name}. \n")
print("Have a nice day!")