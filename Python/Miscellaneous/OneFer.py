def Speak(name = None):
    return f'One for {"you" if name == None else name}, one for me'

print(Speak("Caleb"))

