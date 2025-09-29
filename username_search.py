import requests


def run():
    username = input("enter a username: ")
    print(f" searching '{username}' ")

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
                print(f" found on {platform}: {url}")
            elif r.status_code == 404:
                print(f" not found on {platform}")
            else:
                print(f"? {platform}: status {r.status_code}")
        except Exception as e:
            print(f"Error on {platform}: {e}")