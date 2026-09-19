import os

import pytest

from pages.login_page import LoginPage

@pytest.mark.smoke
@pytest.mark.parametrize(
    "usuario,contrasena,resultado_esperado",
    [
        ("tomsmith","SuperSecretPassword!","exito"),
        ("tomsmith","password_incorrecta","error"),
        ("usuario_invalido","SuperSecretPassword!","error")
    ],
    ids=["login_valido","password_incorrecto","username_invalido"]

)
def test_login(navegador,usuario,contrasena,resultado_esperado):
    try:
        login_page=LoginPage(navegador)
        login_page.login(usuario,contrasena)
    except Exception as e:
        pytest.fail(f"Error durante el login: {e}")

    if resultado_esperado=="exito":
        assert "secure" in navegador.current_url,(
            f" Se esperaba login exitoso. URL actual: {navegador.current_url}"
        )
    else:
        os.makedirs("imagenes", exist_ok=True)
        navegador.save_screenshot(f"imagenes/fallo_{usuario}.png")
        assert "secure" not in  navegador.current_url,(
            f"No se esperaba login exitoso. pero redirigio a :{navegador.current_url}"
        )