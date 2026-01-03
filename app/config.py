import os

HOST = os.getenv("CAPX_HOST", "0.0.0.0")
PORT = int(os.getenv("CAPX_PORT", "8000"))