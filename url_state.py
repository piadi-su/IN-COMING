from urllib.parse import urlparse
import requests

def run():
    def is_url_valid(url):
        try:
            parsed = urlparse(url)
            return parsed.scheme in ('http', 'https') and parsed.hostname is not None
        except Exception:
            return False

    def is_url_online(url, timeout=5):
        try:
            response = requests.head(url, timeout = timeout)
            if 200 <= response.status_code < 400:
                return True
            else:
                return False
        except requests.RequestException:
            return False

    try:
        url = str(input("enter the URL(example: https://www.url.com/): "))
        if is_url_online(url):
            print(f"{url} is online.")
        else:
            print(f"{url} is offline or unreachable.")
    except ValueError:
        print("Please enter a valid URL!")