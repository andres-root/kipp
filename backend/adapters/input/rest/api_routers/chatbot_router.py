from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from backend.core.agents.services import AgentService

chatbot_router = APIRouter(prefix="/chat", tags=["chat"])
agent_service = AgentService()


class ChatBotRequest(BaseModel):
    message: str


@chatbot_router.post("/")
async def chat(request: ChatBotRequest):
    return StreamingResponse(agent_service.chatbot_stream(request.message), media_type="text/event-stream")
