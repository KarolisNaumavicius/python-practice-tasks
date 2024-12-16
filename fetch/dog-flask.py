from flask import Flask, jsonify
import urllib.request
import json 
import ssl

# Sukuriame Flask aplikaciją
app = Flask(__name__)

# Sukuriame SSL kontekstą, kuris apeina sertifikato tikrinimą
context = ssl._create_unverified_context()

@app.route('/get-dog-image', methods=['GET'])
def get_dog_image():
    try: 
        # API URL
        url = "https://dog.ceo/api/breeds/image/random"

        # Siunčiame GET užklausą su SSL kontekstu
        with urllib.request.urlopen(url, context=context) as response:
            data = response.read()

        # Dekoduojame JSON atsakymą
        result = json.loads(data)

        # Ištraukiame šuns nuotraukos URL
        image_url = result["message"]

        # Grąžiname JSON atsakymą vartotojui
        return jsonify({"dog_image_url": image_url})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Paleidžiame Flask serverį
if __name__ == '__main__':
    app.run(debug=True)