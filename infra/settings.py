from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_address: str = Field(..., env="SERVER_ADDRESS")

    keycloak_url: str = Field(..., env="KEYCLOAK_URL")
    keycloak_client_id: str = Field(..., env="KEYCLOAK_CLIENT_ID")
    keycloak_client_secret_key: str = Field(..., env="KEYCLOAK_CLIENT_SECRET_KEY")
    keycloak_admin_client_secret: str = Field(..., env="KEYCLOAK_ADMIN_CLIENT_SECRET")
    keycloak_realm: str = Field(..., env="KEYCLOAK_REALM")
    keycloak_callback_uri: str = Field(..., env="KEYCLOAK_CALLBACK_URI")

    minio_url: str = Field(..., env="MINIO_URL")
    minio_access_key: str = Field(..., env="MINIO_ACCESS_KEY")
    minio_secret_key: str = Field(..., env="MINIO_SECRET_KEY")
    minio_session_token: str = Field(..., env="MINIO_SESSION_TOKEN")
    minio_region_name: str = Field(..., env="MINIO_REGION_NAME")
    minio_verify: str = Field(..., env="MINIO_VERIFY")
    minio_secure: bool = Field(..., env="MINIO_SECURE")
    minio_bucket: str = Field(..., env="MINIO_BUCKET")

    postgres_username: str = Field(..., env="POSTGRES_USERNAME")
    postgres_password: str = Field(..., env="POSTGRES_PASSWORD")
    postgres_host: str = Field(..., env="POSTGRES_HOST")
    postgres_port: str = Field(..., env="POSTGRES_PORT")
    postgres_database: str = Field(..., env="POSTGRES_DATABASE")

    def get_postgres_url(self) -> str:
        return (
            f"postgresql+asyncpg:"
            f"//{self.postgres_username}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_database}"
        )

    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: str = Field(..., env="REDIS_PORT")

    def get_redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"

    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"


settings = Settings()
