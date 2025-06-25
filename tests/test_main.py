from pydantic_settings import CliApp

from typer_demo import Settings


def test_main():
    settings = CliApp.run(Settings)
    assert settings.name == "World"
