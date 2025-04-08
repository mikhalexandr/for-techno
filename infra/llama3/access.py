from infra.llama3.client import Llama3Client


async def init_llama3_client() -> None:
    await Llama3Client.init_client()


async def close_llama3_client() -> None:
    await Llama3Client.close_client()


async def get_llama3_client() -> 'Llama3Client':
    return Llama3Client.get_instance()
