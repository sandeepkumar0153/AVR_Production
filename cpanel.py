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
    """ A simple echo client """ 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address) 
     
    # Send data 
    try: 
        # Send data 
        message = "Test message. This will be 
                   echoed" 
        print ("Sending %s" % message) 
        sock.sendall(message.encode('utf-8')) 
        # Look for the response 
        amount_received = 0 
        amount_expected = len(message) 
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Received: %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Closing connection to the server") 
        sock.close() 
     
if __name__ == '__main__': 
    parser = argparse.ArgumentParser
            (description='Socket Server Example') 
    parser.add_argument('--port', action="store", 
dest="port", type=int, required=True) 
    given_args = parser.parse_args()  
    port = given_args.port 
    echo_client(port) 
