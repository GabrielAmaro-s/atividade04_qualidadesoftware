import os

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def pagina():
    with sync_playwright() as automacao:
        configuracao = {"headless": True}
        caminho_executavel = os.getenv("CAMINHO_CHROMIUM")
        if caminho_executavel:
            configuracao["executable_path"] = caminho_executavel
        navegador = automacao.chromium.launch(**configuracao)
        aba = navegador.new_page()
        yield aba
        navegador.close()
