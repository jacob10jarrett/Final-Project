import uvicorn
import schemas
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .models import model_loader
from .controllers import customers, reviews
from .dependencies.config import conf
from .dependencies.database import engine, get_db


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)