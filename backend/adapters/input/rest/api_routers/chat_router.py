from fastapi import APIRouter
from pydantic import BaseModel

chat_router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    prompt: str


@chat_router.post("/")
def chat(request: ChatRequest):
    return {"message": "Hello from chat!", "prompt": request.prompt}
