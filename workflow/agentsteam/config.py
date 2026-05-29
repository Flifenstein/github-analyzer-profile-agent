# config.py
import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

# fail fast if something's missing
if not all([ANTHROPIC_API_KEY, GITHUB_TOKEN, GITHUB_USERNAME]):
    raise ValueError("Missing required environment variables — check your .env")