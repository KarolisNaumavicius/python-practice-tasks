import urllib.request 
import json
import ssl

# API URL

url = "http://dog.ceo/api/breeds/image/random"

# Sukuriame SSL sertifikato konteksta, kuris aplenkia sertifikato tikrinima

context = ssl._create_unverified_context()

# Sukuriame Request objekta su GET metodu

request = urllib.request.Request(url, method='GET')

# Siunciame GET uzklausa

with urllib.request.urlopen(request, context=context) as response:
    data = response.read()

# Dekoduojame JSON atsakyma
result = json.loads(data)

# Istraukiame suns nuotraukas URL
image_url = result["message"]

print("Dog image URL", image_url)

