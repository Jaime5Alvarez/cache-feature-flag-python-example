from dotenv import load_dotenv
import os

load_dotenv()

POSTHOG_API_KEY = os.getenv("POSTHOG_API_KEY")

if not POSTHOG_API_KEY:
    raise ValueError("POSTHOG_API_KEY is not set")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
