from fastapi_keycloak import FastAPIKeycloak

from infra.keycloak_.client import KeycloakClient


async def init_keycloak_client() -> None:
    await KeycloakClient.init_client()


async def close_keycloak_client() -> None:
    await KeycloakClient.close_client()


async def get_keycloak_client() -> FastAPIKeycloak:
    return KeycloakClient.get_client()
