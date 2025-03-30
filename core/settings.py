from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_address: str = Field(..., env="SERVER_ADDRESS")

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

    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: str = Field(..., env="REDIS_PORT")

    class Config:
        env_file = "./.env"
        env_file_encoding = "utf-8"

    def get_postgres_url(self) -> str:
        return (
            f"postgresql+asyncpg:"
            f"//{self.postgres_username}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_database}"
        )

    def get_redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"


settings = Settings()
