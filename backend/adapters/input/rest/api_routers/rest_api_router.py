from fastapi import APIRouter

from backend.adapters.input.rest.api_routers.chatbot_router import chatbot_router

router = APIRouter(prefix="/api/v1", tags=["api", "rest"])

router.include_router(chatbot_router)
