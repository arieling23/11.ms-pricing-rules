from dotenv import load_dotenv
import os

load_dotenv()  # ✅ Cargar variables del archivo .env

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
PORT = int(os.getenv("PORT", 8081))
