import socket

def run():
    def url_ip(url):
        try:
            ip = socket.gethostbyname(url)
            return ip
        except socket.gaierror:
            return f"Unable to find IP for: {url}"

    url = input("Enter the URL(example:domain.com): ")
    ip = url_ip(url)
    print(f"the ip of {url} is: {ip}")