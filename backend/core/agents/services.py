from typing import AsyncGenerator

from backend.core.agents.calendar_agent import CalendarAgent, CalendarAgentResponse
from backend.core.agents.chatbot_agent import ChatBotAgent


class AgentService:
    def __init__(self):
        self.calendar_agent = CalendarAgent()
        self.chatbot_agent = ChatBotAgent()

    async def chatbot_stream(self, message: str) -> AsyncGenerator[str, None]:
        async for chunk in self.chatbot_agent.stream(message):
            yield chunk

    def parse_event(self, prompt: str) -> CalendarAgentResponse:
        event = self.calendar_agent.run(prompt)
        if not event:
            raise ValueError("Invalid event response")
        print("DEBUG: ", event)
        return event
