import secrets

url_safe_token = secrets.token_urlsafe(17)
print(f"Secure Token: {url_safe_token}")