savefile = open("savefile.txt", "r")

savefilelines = savefile.readlines()

health = int(savefilelines[0])
age = int(savefilelines[1])
happiness = int(savefilelines[2])
hungerlevel = int(savefilelines[3])

savefile.close()

health += 1
