from dotenv import load_dotenv
import os

load_dotenv()

print("API Key:", os.getenv("GROQ_API_KEY"))
print("Model:", os.getenv("MODEL_NAME"))