import os
import subprocess
import requests
import socket
import time


#main functions
def search_username():
    username = input("Inserisci username: ")
    print(f"🔎 Cerco '{username}' sui social...")

    social_urls = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter/X": f"https://x.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Telegram": f"https://t.me/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "GitHub": f"https://github.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "4chan": f"https://boards.4channel.org/search#/text/{username}",
        "StackOverflow": f"https://stackoverflow.com/users/story/{username}",
        "Quora": f"https://www.quora.com/profile/{username}"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36"
    }

    for platform, url in social_urls.items():
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                print(f" Trovato su {platform}: {url}")
            elif r.status_code == 404:
                print(f" Non trovato su {platform}")
            else:
                print(f"❔ {platform}: status {r.status_code}")
        except Exception as e:
            print(f"Errore su {platform}: {e}")


def ip_analysis():
    print("IP Geolocate Tool")
    ip = input("Enter an IP address: ")
    url = f"https://ipinfo.io/{ip}/json"

    try:
        response = requests.get(url)
        response.raise_for_status()

        print("Request successfully made:")

        data = response.json()

        print("\n--- IP Info ---")
        print(f"Country: {data.get('country')}")
        print(f"City: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"ASN: {data.get('org')}")
        print(f"Postal Code: {data.get('postal')}")
        print(f"Coordinates: {data.get('loc')}")

        loc = data.get('loc')
        if loc:
            lat, lon = loc.split(',')
            print(f"Google Maps: https://www.google.com/maps/?q={lat},{lon}")

    except requests.RequestException as e:
        print(f"Error: {e}")



while True:

      time.sleep(2)
      print("")
      print("""
      ██╗███╗   ██╗       ██████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
      ██║████╗  ██║      ██╔════╝██╔═══██╗████╗ ████║██║████╗  ██║██╔════╝ 
      ██║██╔██╗ ██║█████╗██║     ██║   ██║██╔████╔██║██║██╔██╗ ██║██║  ███╗
      ██║██║╚██╗██║╚════╝██║     ██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
      ██║██║ ╚████║      ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
      ╚═╝╚═╝  ╚═══╝       ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ """)


      print("""
            1. username search
            2. IP analysis 
            0. exit """)
      choise_1 = input("->choise: ")



      if choise_1 == "1":
            search_username()

      elif choise_1 == "2":
            ip_analysis()

      elif choise_1 == "0":
          break

      else:
          print("chose one of the options!")