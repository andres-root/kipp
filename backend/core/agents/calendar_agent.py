from pydantic import BaseModel

from backend.adapters.output.ai.langchain_adapter import LangchainAdapter
from backend.core.agents.base_agent import BaseAgent


class CalendarAgentResponse(BaseModel):
    title: str | None = None
    description: str | None = None
    start_datetime: str | None = None
    end_datetime: str | None = None
    location: str | None = None
    timezone: str | None = None


class CalendarAgent(BaseAgent):
    def __init__(self):
        self.model_adapter = LangchainAdapter()
        self.prompt_name = "calendar-data-extractor"

    def run(self, prompt: str) -> CalendarAgentResponse | str | dict:
        return self.model_adapter.invoke(
            self.prompt_name, response_model=CalendarAgentResponse, params={"schedule_message": prompt}
        )
