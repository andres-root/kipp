from fastapi import FastAPI

from backend.adapters.input.rest.api_routers.rest_api_router import router

app = FastAPI()
app.include_router(router)
