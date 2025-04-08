from keycloak import KeycloakOpenID

from infra.logger import logger
from infra.settings import settings


class KeycloakClient:
    _client: KeycloakOpenID | None = None

    @classmethod
    async def init_client(
            cls
    ) -> None:
        if cls._client is not None:
            logger.error("Keycloak is already initialized")
            return None

        cls._client = KeycloakOpenID(
            server_url=settings.keycloak_server_url,
            client_id=settings.keycloak_client_id,
            client_secret_key=settings.keycloak_client_secret_key,
            realm_name=settings.keycloak_realm_name,
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
    ) -> KeycloakOpenID:
        return cls._client
