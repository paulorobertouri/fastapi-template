from os import getenv

import uvicorn
from dotenv import load_dotenv

from app.create_app import create_app

load_dotenv()

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=getenv("HOST", "0.0.0.0"),
        port=int(getenv("PORT", "8000")),
        reload=getenv("FASTAPI_ENV", "development") != "production",
    )
