import speech_recognition as sr
import time
from multiprocessing import Process
from Voice_Recognition import start_listening

class ForeverListener():
    def __init__(self, still_listening=True):
        self.still_listening = still_listening

    def listen_for_keyword(self):
        # get audio from the microphone                                                                       
        r = sr.Recognizer()                    
        keyword = "Zelda"                                                                
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = r.listen(source)

        # See if audio contains keyword - if not, try again
        try:
            if  r.recognize_google(audio).find(keyword) != -1:
                print("woohoo!")
                print('\a') # Ding!
                start_listening()
            else:
                print("aww")
                print(r.recognize_google(audio))
                self.listen_for_keyword()

        except sr.UnknownValueError:
            print("Could not understand audio")
            self.listen_for_keyword()
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            self.listen_for_keyword()

if __name__ == '__main__':
    Zelda = ForeverListener()
    Zelda.listen_for_keyword()