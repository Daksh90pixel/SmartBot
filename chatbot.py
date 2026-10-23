import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Check your .env file.")

client = genai.Client(api_key=api_key)


def get_response(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )

        return response.text or "I couldn't generate a response."

    except Exception as e:
        print("Gemini API Error:", e)
        return "Sorry, I'm having trouble connecting. Please try again."