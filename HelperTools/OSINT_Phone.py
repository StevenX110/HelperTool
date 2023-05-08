import time
import sys
import requests
import json
import time
import urllib.request, urllib.parse, urllib.error
import os
text = "Hi.. Oh, you have just decided to look over your own abilities? Sounds flawlessly.. Take it as lesson, where u are looking beyond your power.. I hope, it will help you. Heh, anyway, you will have gotten more power by the end of your studying.. Enjoy =)"
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)     
    if text.index(char) == len(text)-1:        
     print("\n")
class Config:
    key = "Ap1afiWIKKVynFvSleSkVq23ZG2dUIxV"

def main():
    print("Oh, heh, it's my 2nd creature that was made by me")
    print("________________________")
    print("\n____________________")
    print("\n________________")
    print("\n_____________")
    print("\n____________")
    print("\n__________")
    print("\n________")
    print("\n______")
    print("\n1. Press 1 if you want to search by number")

import requests
import json
import time

class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'

class Config:
    key = "Ap1afiWIKKVynFvSleSkVq23ZG2dUIxV"

while True:
    if input('Hey, choose number:') == '1':
        number = input('Enter phone number: ')
        api = "http://apilayer.net/api/validate?access_key=" + Config.key + "&number=" + number + "&country_code=&format=1"
        output = requests.get(api)
        content = output.text
        obj = json.loads(content)
        try:
            country_code = obj['country_code']
            country_name = obj['country_name']
            location = obj['location']
            carrier = obj['carrier']
            line_type = obj['line_type']
        except KeyError:
            print(Color.RED + "[-] " + Color.END + "Uh.. it hasn't found anything")
            continue
        print(Color.YELLOW + "[+] " + Color.END + "Phone number information gathering -- Firefly")
        print("--------------------------------------")
        time.sleep(0.2)
        if country_code == "":
            print(" - Getting Country        [ " + Color.RED + "FAILED " + Color.END + "]")
        else:
            print(" - Getting Country        [ " + Color.GREEN + "OK " + Color.END + "]")
        time.sleep(0.2)
        if country_name == "":
            print(" - Getting Country Name        [ " + Color.RED + "FAILED " + Color.END + "]")
        else:
            print(" - Getting Country Name        [ " + Color.GREEN + "OK " + Color.END + "]")
        time.sleep(0.2)
        if location == "":
            print(" - Getting Location        [ " + Color.RED + "FAILED " + Color.END + "]")
        else:
            print(" - Getting Location        [ " + Color.GREEN + "OK " + Color.END + "]")
        time.sleep(0.2)
        if carrier == "":
            print(" - Getting Carrier        [ " + Color.RED + "FAILED " + Color.END + "]")
        else:
            print(" - Getting Carrier        [ " + Color.GREEN + "OK " + Color.END + "]")
        time.sleep(0.2)
        if line_type == None:
            print(" - Getting Device        [ " + Color.RED + "FAILED " + Color.END + "]")
        else:
            print(" - Getting Device        [ " + Color.GREEN + "OK " + Color.END + "]")
