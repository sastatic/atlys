import os
from fastapi import Request, HTTPException, Header

API_KEY = "your-static-api-key"
STATIC_API_KEY=os.getenv('STATIC_API_KEY')

# Dependency function to validate API key
async def authenticate_api_key(request: Request):
    api_key = request.headers.get("api-key")
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return True