#!/usr/bin/env python3

# This is just a test, heavily based off of speech_recognition docs. Designed to send out FB messages when a trigger word is said
# for my own amusement.

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
def audio_rec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        output = r.recognize_sphinx(audio)
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        return output
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

def main():
    while True:
        out_str = audio_rec()
        check_1 = False
        for word in out_str.split():
            if check_1:
                if word == 'times' or word == 'time':
                    print("Send FB message here")
                else:
                    check_1 = False
            if word == 'good':
                check_1 = True

main()
