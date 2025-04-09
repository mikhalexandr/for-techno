from typing import Dict

from infra.keycloak_.client import KeycloakClient


async def init_keycloak_client() -> None:
    await KeycloakClient.init_client()


async def close_keycloak_client() -> None:
    await KeycloakClient.close_client()


async def authenticate() -> Dict:
    return KeycloakClient.authenticate()
