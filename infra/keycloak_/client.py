from fastapi_keycloak import FastAPIKeycloak

from infra.logger import logger
from infra.settings import settings


class KeycloakClient:
    _client: FastAPIKeycloak | None = None

    @classmethod
    async def init_client(
            cls
    ) -> None:
        if cls._client is not None:
            logger.error("Keycloak is already initialized")
            return None

        cls._client = FastAPIKeycloak(
            server_url=settings.keycloak_url,
            client_id=settings.keycloak_client_id,
            client_secret_key=settings.keycloak_client_secret_key,
            admin_client_secret=settings.keycloak_admin_client_secret,
            realm=settings.keycloak_realm,
            callback_uri=settings.keycloak_callback_uri
        )
        logger.info("Keycloak initialized")

    @classmethod
    async def close_client(
            cls
    ) -> None:
        if cls._client is not None:
            cls._client = None
            logger.info("Keycloak closed")

    @classmethod
    def get_client(
            cls
    ) -> FastAPIKeycloak:
        return cls._client
