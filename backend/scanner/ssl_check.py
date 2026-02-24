import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime


def check_ssl(url):
    parsed = urlparse(url)
    hostname = parsed.hostname

    ssl_info = {
        "SSL Valid": False,
        "Expiry Date": None,
        "Days Remaining": None
    }

    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                ssl_info["SSL Valid"] = True

                expiry = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
                ssl_info["Expiry Date"] = expiry.strftime("%Y-%m-%d")

                days_left = (expiry - datetime.utcnow()).days
                ssl_info["Days Remaining"] = days_left

    except:
        pass

    return ssl_info