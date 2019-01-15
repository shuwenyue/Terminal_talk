from voice import Voice
import speech_recognition as sr
from commandfactory import CommandFactory

#dkdljf
r = sr.Recognizer()
mic = sr.Microphone()

while True:
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print('Say something')
            audio = r.listen(source)
        try:
            cmdString = r.recognize_google(audio).lower()
            print(cmdString)
            if cmdString == 'exit' or cmdString == 'quit' or cmdString == 'stop':
                print('Quitting')
                break
            v = Voice(cmdString) # define voice object
            try:
                f = CommandFactory(v) # define command factory object
                c = f.getcmdobj() # determine which class to use based on that command
                error = c.run() # run command in appropriate class
                if error == 1:
                    print('Request failed')
            except ValueError:
                # If word not recognized
                print('That was not a valid command')
        except sr.UnknownValueError:
            print('Could not understand, try again')
    except KeyboardInterrupt:
        print('Quitting')
        break
