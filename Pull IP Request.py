import requests

# * * * * *

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "version": response.get("version"),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country"),
        "country_name": response.get("country_name"),
        "country_capital": response.get("country_capital"),
        "postal": response.get("postal"),
        "languages": response.get("languages"),
        "hostname": response.get("hostname")
    }
    return location_data


# hola esto es un cambio
print(get_location())
