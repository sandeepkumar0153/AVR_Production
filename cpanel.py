from http.server import HTTPServer
from sqlalchemy import create_engine
import os
import socket
import sys
import argparse

host = 'localhost'
data_payload = 3001
backlog = 5

db_url = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/mydatabase')
# DATABASE_URL uses postgres:// but SQLAlchemy only accepts postgresql://
db_url = db_url.replace('postgres://', 'postgresql://')

# Get port number from the PORT environment varaible or 3000 if not specified
port = os.getenv('PORT', 3000)

server = HTTPServer(('0.0.0.0', port), MyServer)
server.serve_forever()

engine = create_engine(db_url)
...

with engine.connect() as connection:
    result = connection.execute(...)
...

def start_app(port):
        """ A simple echo server """
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, 
                          socket.SOCK_STREAM)
        # Enable reuse address/port 
        sock.setsockopt(socket.SOL_SOCKET, 
                      socket.SO_REUSEADDR, 1)
        # Bind the socket to the port
        server_address = (host, port)
        print ("Starting up echo server  on %s 
                     port %s" % server_address)
        sock.bind(server_address)
        # Listen to clients, backlog argument 
          specifies the max no. 
          of queued connections
        sock.listen(backlog) 
        while True: 
            print ("Waiting to receive message 
                    from client")
            client, address = sock.accept() 
            data = client.recv(data_payload) 
            if data:
                print ("Data: %s" %data)
                client.send(data)
                print ("sent %s bytes back 
                       to %s" % (data, address))
            # end connection
            client.close() 
    
    if __name__ == '__main__':
        parser = argparse.ArgumentParser
        (description='Socket Server Example')
        parser.add_argument('--port', 
        action="store", dest="port", type=int, 
                           required=True)
        given_args = parser.parse_args() 
        port = given_args.port
        echo_server(port)    
   
