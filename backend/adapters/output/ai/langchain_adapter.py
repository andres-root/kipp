import logging

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langsmith import Client
from pydantic import BaseModel

from backend.settings import get_settings

settings = get_settings()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class LangchainAdapter:
    def __init__(self):
        self.langsmith_client = Client(api_key=settings.langsmith_api_key)
        self.anthropic = ChatAnthropic(
            api_key=settings.anthropic_api_key,
            model="claude-3-5-haiku-20241022",
            temperature=1,
            max_tokens=1000,
        )
        self.openai = ChatOpenAI(
            api_key=settings.openai_api_key,
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

    def get_chain(self, prompt_name: str, response_model: BaseModel = None, params: dict = None):
        try:
            prompt = self.langsmith_client.pull_prompt(prompt_name)
            chain = prompt | self.model

            return chain
        except Exception as e:
            logger.error(f"Error streaming model: {e}")
            return None
