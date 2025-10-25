from fastapi import Depends, Header, HTTPException, status

API_KEY = "demo-key"

def api_key_auth(x_api_key: str | None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")
    return True
