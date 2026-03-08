import os
import random
import string
import requests
from colorama import Fore, init
import pyshorteners

init(autoreset=True)

def clear():
    os.system("clear")

def banner():
    print(Fore.MAGENTA + """
========================================
        AKASH INSTAGRAM TOOLKIT
========================================
""")

def menu():
    print(Fore.CYAN + """
[1] Instagram Profile Info
[2] Username Generator
[3] Caption Generator
[4] Hashtag Generator
[5] Password Generator
[6] IP Lookup
[7] URL Shortener
[0] Exit
""")

def profile_info():

    username = input("Enter Instagram username: ")

    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*"
    }

    try:

        r = requests.get(url, headers=headers)

        if r.status_code != 200:
            print("Request blocked by Instagram")
            return

        data = r.json()

        user = data["data"]["user"]

        print("\nUsername:", user["username"])
        print("Full Name:", user["full_name"])
        print("Followers:", user["edge_followed_by"]["count"])
        print("Following:", user["edge_follow"]["count"])
        print("Posts:", user["edge_owner_to_timeline_media"]["count"])
        print("Private:", user["is_private"])
        print("Verified:", user["is_verified"])
        print("Bio:", user["biography"])

    except:
        print("Failed to fetch profile")

def username_gen():

    base = input("Base word: ")

    print("\nGenerated usernames:\n")

    for i in range(20):

        num = random.randint(100,9999)

        symbol = random.choice(["_",".",""])

        print(base + symbol + str(num))

def caption_gen():

    captions = [
        "Dream big work hard.",
        "Stay real stay humble.",
        "Create your own vibe.",
        "Life is short make it viral.",
        "Focus hustle repeat.",
        "New post new vibe."
    ]

    print("\nCaption:\n")

    print(random.choice(captions))

def hashtag_gen():

    tags = [
        "#instagram",
        "#reels",
        "#viral",
        "#explorepage",
        "#trending",
        "#instagood",
        "#socialmedia",
        "#contentcreator"
    ]

    print("\nHashtags:\n")

    print(" ".join(tags))

def password_gen():

    length = int(input("Password length: "))

    chars = string.ascii_letters + string.digits + "!@#"

    password = "".join(random.choice(chars) for i in range(length))

    print("\nPassword:", password)

def ip_lookup():

    ip = input("Enter IP: ")

    try:

        r = requests.get(f"http://ip-api.com/json/{ip}").json()

        print("\nCountry:", r["country"])
        print("City:", r["city"])
        print("ISP:", r["isp"])

    except:

        print("Lookup failed")

def url_short():

    link = input("Enter URL: ")

    try:

        s = pyshorteners.Shortener()

        short = s.tinyurl.short(link)

        print("\nShort URL:", short)

    except:

        print("Failed")

while True:

    clear()

    banner()

    menu()

    choice = input("\nSelect option: ")

    if choice == "1":

        profile_info()

    elif choice == "2":

        username_gen()

    elif choice == "3":

        caption_gen()

    elif choice == "4":

        hashtag_gen()

    elif choice == "5":

        password_gen()

    elif choice == "6":

        ip_lookup()

    elif choice == "7":

        url_short()

    elif choice == "0":

        break

    input("\nPress Enter to continue...")
