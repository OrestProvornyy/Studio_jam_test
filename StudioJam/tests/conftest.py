import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = "D:/PyCharm Community Edition 2024.3.4/MyProjects/StudioJam/driver/chromedriver.exe"

@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver
    time.sleep(10)
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return "https://9ba8-194-44-56-142.ngrok-free.app"