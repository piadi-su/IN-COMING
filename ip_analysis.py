import requests

def run():
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


#ip analysis