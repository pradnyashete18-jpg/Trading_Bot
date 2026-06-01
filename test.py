# test_env.py

from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("API_KEY"))
print(os.getenv("API_SECRET"))