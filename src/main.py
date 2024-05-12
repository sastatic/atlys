import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from app.routes import v1_scraping_routes
from app.middleware.authentication import authenticate_api_key

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

app = FastAPI()
app.include_router(v1_scraping_routes.router, prefix="/api/v1")

# Apply authentication middleware globally
@app.middleware("http")
async def apply_authentication(request, call_next):
    if request.url.path.startswith("/api/v1"):
        await authenticate_api_key(request)
    response = await call_next(request)
    return response


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.getenv('SERVER_HOST'),
        port=int(os.getenv('SERVER_PORT')),
        log_level=os.getenv('LOG_LEVEL')
    )