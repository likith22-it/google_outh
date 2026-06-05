from authlib.integrations.requests_client import OAuth2Session
from dotenv import load_dotenv
import os

from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"

print("Looking for .env at:", env_path)
print("Exists?", env_path.exists())


load_dotenv(dotenv_path="C:/Users/Admin/Desktop/assign2/.env")
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
USER_INFO = "https://www.googleapis.com/oauth2/v1/userinfo"

REDIRECT_URI = "http://localhost:8501"

def get_google_auth():
    return OAuth2Session(
        CLIENT_ID,
        CLIENT_SECRET,
        scope="openid email profile",
        redirect_uri=REDIRECT_URI
    )

def get_auth_url():
    google = get_google_auth()
    uri, _ = google.create_authorization_url(AUTH_URL)
    return uri

def get_token(code):
    google = get_google_auth()
    return google.fetch_token(TOKEN_URL, code=code)

def get_user_info(token):
    google = OAuth2Session(CLIENT_ID, token=token)
    return google.get(USER_INFO).json()

print("CLIENT_ID:", CLIENT_ID)