import gtts
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('age', 80)
#change gender of voice!
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

while(True):
    choice = int(input("Choose any of the following: \n1. Text to speech\n2. Increase volume\n3. Decrease Volume\n4. Exit\n"))
    if (choice == 1):
        sentence = input("Enter sentence to be converted: \n")
        engine.say(sentence)
        engine.runAndWait()
    elif (choice == 2):
        vol = engine.getProperty("volume")
        if (vol == 1.0):
            print("Maximum volume!")
        else:
            engine.setProperty("volume", vol+0.2)
            print("Volume Increased")
    elif (choice == 3):
        vol = engine.getProperty("volume")
        if (vol == 0.0):
            print("Minimum volume!")
        else:
            engine.setProperty("volume", vol-0.2)
            print("Volume Decreased!")
    elif (choice == 4):
        print("Bye!")
        break
    else:
        print("Invalid Input!")

