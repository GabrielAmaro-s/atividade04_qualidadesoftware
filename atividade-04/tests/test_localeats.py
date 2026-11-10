
from playwright.sync_api import expect


def test_abrir_formulario_de_cadastro(pagina):
    pagina.goto(
        "https://local-eats-unisenac.vercel.app/static/login.html",
        wait_until="load"
    )

    botao_cadastro = pagina.get_by_role(
        "button", name="Criar Conta", exact=True
    )

    expect(botao_cadastro).to_be_visible()
    botao_cadastro.click()

    expect(pagina.locator("#registerForm")).to_be_visible(timeout=10000)
    expect(pagina.locator("#regName")).to_be_visible()
    expect(pagina.get_by_role("button", name="Registrar", exact=True)).to_be_visible()
