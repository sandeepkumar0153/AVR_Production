from http.server import HTTPServer
from sqlalchemy import create_engine
import os

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

def start_app():
   print "hello from the_function"
