from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_address: str = Field(..., env="SERVER_ADDRESS")

    keycloak_server_url: str = Field(..., env="KEYCLOAK_SERVER_URL")
    keycloak_client_id: str = Field(..., env="KEYCLOAK_CLIENT_ID")
    keycloak_client_secret_key: str = Field(..., env="KEYCLOAK_CLIENT_SECRET_KEY")
    keycloak_realm_name: str = Field(..., env="KEYCLOAK_REALM_NAME")
    keycloak_token_url: str = Field(..., env="KEYCLOAK_TOKEN_URL")

    llama3_api_url: str = Field(..., env="LLAMA3_API_URL")
    llama3_model: str = Field(..., env="LLAMA3_MODEL")

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

    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"


settings = Settings()
