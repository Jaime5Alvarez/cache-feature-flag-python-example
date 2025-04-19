from dotenv import load_dotenv
import os

load_dotenv()

POSTHOG_API_KEY = os.getenv("POSTHOG_API_KEY")

if not POSTHOG_API_KEY:
    raise ValueError("POSTHOG_API_KEY is not set")
