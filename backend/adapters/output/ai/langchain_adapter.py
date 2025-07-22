import logging

from django.conf import settings
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langsmith import Client
from pydantic import BaseModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class LangchainAdapter:
    def __init__(self):
        self.langsmith_client = Client(api_key=settings.LANGSMITH_API_KEY)
        self.anthropic = ChatAnthropic(
            api_key=settings.ANTHROPIC_API_KEY,
            model="claude-3-5-haiku-20241022",
            temperature=1,
            max_tokens=1000,
        )
        self.openai = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model="gpt-4o-mini",
            temperature=1,
        )
        self.model = self.openai

    def invoke(self, prompt_name: str, response_model: BaseModel, params: dict) -> dict | BaseModel:
        try:
            prompt = self.langsmith_client.pull_prompt(prompt_name)
            chain = prompt | self.model
            result = chain.invoke(params)
            return result
        except Exception as e:
            logger.error(f"Error invoking model: {e}")
            return None

    async def stream(
        self, prompt_name: str, response_model: BaseModel, params: dict
    ) -> AsyncGenerator[dict | BaseModel, None]:
        try:
            prompt = self.langsmith_client.pull_prompt(prompt_name)
            chain = prompt | self.model

            async for chunk in chain.stream(params):
                yield chunk
        except Exception as e:
            logger.error(f"Error streaming model: {e}")
            return None
