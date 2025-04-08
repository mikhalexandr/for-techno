import aiohttp
import json
from pydantic import BaseModel

from infra.logger import logger
from infra.settings import settings


class Message(BaseModel):
    model: str
    prompt: str
    stream: bool


class Response(BaseModel):
    model: str
    response: str
    done: bool


class Llama3Client:
    api_url: str | None = None

    @classmethod
    async def init_client(
            cls
    ) -> None:
        if cls.api_url is not None:
            logger.error("Llama3 is already initialized")
            return None

        cls.api_url = settings.llama3_api_url
        logger.info("Llama3 initialized")

    @classmethod
    async def close_client(
            cls
    ) -> None:
        if cls.api_url is not None:
            cls.api_url = None
        logger.info("Llama3 closed")

    @classmethod
    async def send_request(
            cls,
            instruction: str,
            message: str
    ) -> str:
        body = Message(
            model=settings.llama3_model,
            prompt=f"INSTRUCTIONS FOR MODEL: {instruction} | MESSAGE FROM USER -> {message}",
            stream=False
        ).model_dump_json()
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=cls.api_url,
                    headers={"Content-Type": "application/json"},
                    data=body
            ) as response:
                response_text = await response.text()
                response.raise_for_status()
        response_data = json.loads(response_text)
        parsed_response = Response(**response_data)
        return parsed_response.response

    @classmethod
    def get_instance(
            cls
    ) -> 'Llama3Client':
        return cls()
