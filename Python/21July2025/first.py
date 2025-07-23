class Demo1:
    a = 0
    b = 0
    def __init__(self, x, y=None, z=None):
        print(x)
        print(y)
        print(z)

import time

class BasicPhone:
    def makecall(self, number):
        print(f"Calling {number}...")
        time.sleep(2)
        print("Call ended.")
    def sms(self, number):
        message = input("Enter your message: ")
        print(f"Sending SMS to {number}: {message}")
        time.sleep(1)
        print(f"SMS sent. \n{message}")

class Smartphone(BasicPhone):
    def browse_internet(self, url):
        print(f"Browsing {url}...")
        time.sleep(3)
        print("Browsing completed.")
    
    def take_photo(self):
        print("Taking a photo...")
        time.sleep(1)
        print("Photo taken successfully.")
    
    def play_music(self, song):
        print(f"Playing {song}...")
        time.sleep(2)
        print("Music playback finished.")

print("Welcome to the Phone Demo!")
basic_phone = BasicPhone()
basic_phone.makecall("1234567890")
basic_phone.sms("1234567890")
smartphone = Smartphone()
smartphone.browse_internet("www.example.com")
smartphone.take_photo()
smartphone.play_music("song.mp3")

