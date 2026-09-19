# Pytest Demo Login

Framework de automatización de pruebas web con **Python**, **Pytest** y **Selenium**, usando el patrón **Page Object Model (POM)**. Incluye integración continua con **GitHub Actions**.

## Tecnologías

- Python 3
- Pytest
- Selenium
- webdriver-manager
- pytest-html (reportes)
- GitHub Actions (CI)

## Estructura del proyecto

```
aut-framework/
├── .github/workflows/
│   └── tests.yml        # Pipeline de CI
├── pages/
│   └── login_page.py    # Page Object de la página de login
├── tests/
│   └── test_login.py    # Casos de prueba de login
├── conftest.py          # Fixtures compartidas (driver)
├── pytest.ini           # Configuración de Pytest
└── requirements.txt     # Dependencias
```

## Requisitos previos

- Python 3.10 o superior
- Google Chrome instalado
- Git

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/rossileidys1990/aut-framework.git
cd aut-framework
```

2. Crear y activar el entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

En macOS/Linux:

```bash
source venv/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

Correr todas las pruebas:

```bash
pytest
```

Correr un archivo específico:

```bash
pytest tests/test_login.py
```

## Reportes

Al finalizar la ejecución se genera un reporte HTML en `reportes/reporte.html`.

## Integración continua

El workflow `.github/workflows/tests.yml` se ejecuta en cada push y:

1. Instala las dependencias.
2. Corre las pruebas.
3. Sube el reporte y las capturas de pantalla como artefactos.
4. Envía el reporte por correo.

Para el envío de correo se requieren estos secrets en el repositorio (Settings → Secrets and variables → Actions):

| Secret          | Descripción                                    |
|-----------------|------------------------------------------------|
| `MAIL_USERNAME` | Correo de Gmail que envía el reporte           |
| `MAIL_PASSWORD` | Contraseña de aplicación de Google (16 letras) |

## Sobre este proyecto

Proyecto de práctica desarrollado siguiendo un curso de automatización de pruebas con Selenium y Pytest. Lo mantengo en mi perfil como material de aprendizaje.

Práctica realizada por **Rossileidys Silva** – QA Analyst
GitHub: [@rossileidys1990](https://github.com/rossileidys1990)
