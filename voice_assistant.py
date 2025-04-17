import speech_recognition as sr
import pyttsx3
import webbrowser

def speak(text):

 engine = pyttsx3.init()
 engine.say(text)
 engine.runAndWait()

# add your custom functions here
def process(command):
    if "google" in command.strip().lower():
        webbrowser.open("https://google.com")
    elif "chat gpt" in command.strip().lower():
        webbrowser.open("https://chatgpt.com")




recog = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            recog.adjust_for_ambient_noise(source, duration=0.5)
            speak("I am listening...")
            audio = recog.listen(source, timeout=5, phrase_time_limit=5)
            your_command = recog.recognize_google(audio)
            print("You said:", your_command)

        if your_command.strip().lower() == "steve":
            speak("Steve activated")
            try:
             while True:

              with sr.Microphone() as source:
                recog.adjust_for_ambient_noise(source, duration=0.5)
                speak("Listening for command...")
                audio = recog.listen(source, timeout=5, phrase_time_limit=5)
                your_command = recog.recognize_google(audio)
                print("Command:", your_command)

                if "turn off steve" in your_command.lower():
                    speak("Steve turning off")
                    break  # Stop the loop
                else:
                    process(your_command)
            except sr.UnknownValueError:
                print("Could not understand the command.")
            except Exception as e:
                print("Error in Steve mode:", e)
                print(e)
        if your_command.lower() == "turn off":
                    speak("system turning off")
                    break  # Stop the outer loop
                       

         


    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print("Error:", e)
                  
               
           



