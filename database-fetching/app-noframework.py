import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pymongo import MongoClient
from bson import ObjectId

# Prisijungiame prie MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['test_database']  # Duomenų bazės vardas
collection = db['users']  # Kolekcijos pavadinimas

class RequestHandler(BaseHTTPRequestHandler):
    # POST užklausa - pridėti vartotoją
    def do_POST(self):
        if self.path == '/add-users':
            content_length = int(self.headers['Content-Length'])  # Duomenų dydis
            post_data = self.rfile.read(content_length)  # Nuskaityti užklausos turinį
            try:
                user_data = json.loads(post_data.decode('utf-8'))  # Konvertuoti JSON į Python dict
                result = collection.insert_one(user_data)  # Pridėti į MongoDB
                self.send_response(201)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {'message': 'User added successfully', 'id': str(result.inserted_id)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {'error': str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    # GET užklausa - gauti visus vartotojus
    def do_GET(self):
        if self.path == '/get-users':
            try:
                users = list(collection.find())
                for user in users:
                    user['_id'] = str(user['_id'])  # Konvertuoti ObjectId į string
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(users).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {'error': str(e)}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

