import requests

def get_low():
    low_price = requests.get("https://www.ethgasstationapi.com/api/low")
    return float(low_price.content.decode('UTF-8'))

def get_medium():
    standard_price = requests.get("https://www.ethgasstationapi.com/api/standard")
    return float(standard_price.content.decode('UTF-8'))

def get_high():
    fast_price = requests.get("https://www.ethgasstationapi.com/api/fast")
    return float(fast_price.content.decode('UTF-8'))
