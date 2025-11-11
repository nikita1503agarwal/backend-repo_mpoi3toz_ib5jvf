import builtins
import types
import pytest

from dream_ai_interface import config
from dream_ai_interface.main import (
    menu_image,
    menu_video,
    menu_transcription,
    menu_question,
    afficher_menu,
)


def test_functions_exist():
    assert callable(menu_image)
    assert callable(menu_video)
    assert callable(menu_transcription)
    assert callable(menu_question)


def test_afficher_menu_returns_choice_when_provided():
    assert afficher_menu("1") == "1"
    assert afficher_menu("2") == "2"
    assert afficher_menu("4") == "4"


def test_config_has_at_least_one_key():
    # At least one key (value can be empty string); check dictionary is non-empty
    assert isinstance(config.api_keys, dict)
    assert len(config.api_keys) >= 1


def test_afficher_menu_quit_raises_systemexit():
    with pytest.raises(SystemExit):
        afficher_menu("q")
