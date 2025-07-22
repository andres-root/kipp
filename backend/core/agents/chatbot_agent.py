from typing import AsyncGenerator

from backend.adapters.output.ai.langchain_adapter import LangchainAdapter


class ChatBotAgent:
    def __init__(self):
        self.langchain_adapter = LangchainAdapter()
        self.prompt_name = "chatbot"

    async def stream(self, message: str) -> AsyncGenerator[str, None]:
        chain = self.langchain_adapter.get_chain(self.prompt_name, None, {"message": message})
        async for chunk in chain.astream({"message": message}):
            yield chunk.content
