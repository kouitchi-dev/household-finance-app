

from fastapi import FastAPI
from routers import router
import models


app = FastAPI()
app.include_router(router)