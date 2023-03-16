from http.server import HTTPServer
import os

# Get port number from the PORT environment varaible or 3000 if not specified
port = os.getenv('PORT', 3000)

server = HTTPServer(('0.0.0.0', port), MyServer)
server.serve_forever()
