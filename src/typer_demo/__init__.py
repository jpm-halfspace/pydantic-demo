from uuid import UUID
from pydantic_settings import BaseSettings, CliApp


class Settings(BaseSettings):
    name: str = "World"
    uuid: UUID = UUID("12345678-1234-5678-1234-567812345678")


if __name__ == "__main__":
    settings = CliApp.run(Settings)
    print(settings)
