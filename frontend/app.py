import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.oauth import get_auth_url, get_token, get_user_info
from backend.db import create_table, insert_user

create_table()

st.title("Google OAuth Login")

# Step 1: Show login button
auth_url = get_auth_url()
st.markdown(f"[Login with Google]({auth_url})")

# Step 2: Handle redirect
query_params = st.query_params

if "code" in query_params:
    code = query_params.get("code")

    token = get_token(code)
    user = get_user_info(token)

    email = user["email"]
    google_id = user["id"]

    insert_user(email, google_id)

    st.success(f" Logged in as {email}")