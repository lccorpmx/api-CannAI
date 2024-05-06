from fastapi import FastAPI
from routers import predicciones_route

app = FastAPI()

app.include_router(predicciones_route.router)