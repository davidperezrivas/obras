from server import app
from dotenv import load_dotenv
import os

if os.getenv("MODO") == "PROD":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev", verbose=True)


app.run(port=os.getenv("port"), debug=True)
