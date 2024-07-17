import time
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import pyautogui
import os
from PIL import Image

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
activationword = 'sky'

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand():
    listener = sr.Recognizer()
    print("Listening for Command")

    with sr.Microphone() as source:
        listener.pause_threshold = 2

        input_speech = listener.listen(source)

    try:
        print("recognising speech........")
        query1 = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query1}')

    except Exception as exception:
        print('Jarvis did not quite catch that')
        speak('Jarvis did not quite catch that')
        print(exception)
        return 'None'
    return query1


def search_wikipedia(query=' '):
    searchResults = wikipedia.search(query)
    if not searchResults:
        print('No Wikipedia page found')
        return 'No result received'
    try:
        wikiPage = wikipedia.page(searchResults[0])

    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])

    print(wikiPage.title)

    wikiSummary = str(wikiPage.summary)

    return wikiSummary


if __name__ == '__main__':
    print('All Systems Nominal.....')
    speak('All systems Nominal')

    while True:
        # pass the command as a list
        query = parseCommand().lower().split()

        if query[0] == activationword:
            query.pop(0)

            if 'hello' in query:
                speak('Jarvis says Greetings, all')

        # Navigation
        if query[0] == 'go' and query[1] == 'to':
            speak('Opening.....')
            query = ' '.join(query[2:])
            webbrowser.get('chrome').open_new(query)

        # Wikipedia
        if query[0] == 'what' and query[1] == 'is':
            query = ' '.join(query[2:])
            print('Finding your solution in universal encyclopedia.......')
            speak('Finding your solution in universal encyclopedia')

            speak(search_wikipedia(query))

        # screenshot
        if query[0] == 'take' and query[1] == 'screenshot':
            print("Enter file name ")
            speak("Enter file name")
            fname = input()
            speak("Please sir hold a sec, I am taking the screenshot ")
            time.sleep(5)
            img = pyautogui.screenshot()
            img.save(f'{fname}.png')
            speak("Screenshot saved successfully ")

        # image processing
        if query[0] == 'what' and query[1] == 'do' and query[2] == 'you' and query[3] == 'see':
            from imagedetection import get_gemini_response
            print("Gemini Application")

            image_path = input("Enter the file path of the image: ")

            # Check if the file exists
            if not os.path.isfile(image_path):
                print("Error: File not found")

            # Load the image
            try:
                image = Image.open(image_path)

            except Exception as e:
                print("Error opening image:", e)

            # Get response
            response = get_gemini_response(image)
            print(response)
            speak(response)

        if query[0] == 'create':
            from texttoimage import text_to_image
            text_query = ' '.join(query[2:])
            print("Query:", text_query)
            text_to_image(text_query)

        else:
            from bard import get_gemini_response
            # Convert the query list into a string
            query_string = ' '.join(query)

            # Print the query string
            print("Query:", query_string)

            # Get gemini response
            answer = get_gemini_response(query_string)
            print(answer)
            speak(answer)
