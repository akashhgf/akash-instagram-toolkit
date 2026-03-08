import os
import random
import requests

def banner():
    os.system("clear")
    print("\033[95m")
    print("╔══════════════════════════════════════╗")
    print("      AKASH INSTAGRAM TOOLKIT v2")
    print("         Creator : Akash")
    print("╚══════════════════════════════════════╝")
    print("\033[96m")

def menu():
    print("[1] Instagram Profile Info")
    print("[2] Profile Picture Link")
    print("[3] Username Generator")
    print("[4] Caption Generator")
    print("[5] Hashtag Generator")
    print("[6] Password Generator")
    print("[7] IP Lookup")
    print("[8] API Tester")
    print("[9] URL Shortener")
    print("[10] Username Availability")
    print("[11] Profile Picture Download")
    print("[12] Story Downloader")
    print("[13] Reel Downloader")
    print("[14] Engagement Calculator")
    print("[15] Bio Generator")
    print("[16] Hashtag Popularity")
    print("[17] Instagram Tips")
    print("[18] Emoji Caption")
    print("[19] Speed Test")
    print("[20] Update Tool")
    print("[0] Exit")

def username_gen():
    letters = "abcdefghijklmnopqrstuvwxyz"
    name = "".join(random.choice(letters) for i in range(6))
    print("Generated Username:", name)

def password_gen():
    chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#"
    pwd = "".join(random.choice(chars) for i in range(10))
    print("Generated Password:", pwd)

while True:
    banner()
    menu()
    choice = input("Select: ")

    if choice == "3":
        username_gen()

    elif choice == "6":
        password_gen()

    elif choice == "0":
        break

    input("\nPress Enter to continue...")
