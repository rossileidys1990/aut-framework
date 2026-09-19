import pytest  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options as ChromeOptions  
from selenium.webdriver.firefox.options import Options as FirefoxOptions  
from selenium.webdriver.edge.options import Options as EdgeOptions

NAVEGADOR = "Chrome"
HEADLESS = True  # ponelo en False cuando quieras VER el navegador en local
 
@pytest.fixture()
def navegador():
    if NAVEGADOR == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        if HEADLESS:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif NAVEGADOR == "Firefox":
        options = webdriver.FirefoxOptions()
        if HEADLESS:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif NAVEGADOR == "Edge":
        options = webdriver.EdgeOptions()
        if HEADLESS:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        raise Exception(f"Navegador {NAVEGADOR} no soportado")
 
    driver.set_window_size(1920, 1080)
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()
 