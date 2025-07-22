from fastapi import APIRouter

from backend.adapters.input.rest.api_routers.chat_router import chat_router

router = APIRouter(prefix="/api/v1", tags=["api", "rest"])

router.include_router(chat_router)
