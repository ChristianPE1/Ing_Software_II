import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TestCalculator:
    # Opciones de navegacions
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    title = driver.title

    @classmethod
    def setup_class(cls):
        cls.options.add_argument('--start-maximized')
        cls.options.add_argument('--disable-extensions')
        cls.driver.get("https://www.calculator.net/")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_calculate(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="homelistwrap"]/div[3]/div[2]/a'))).click()

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="content"]/table[2]/tbody/tr/td/div[3]/a'))).click()

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'cpar1'))).send_keys('15')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.ID, 'cpar2'))).send_keys('100')

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[3]/div[1]/form[1]/table/tbody/tr[2]/td/input[2]'))).click()

        resultado = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/p[2]/font/b')
        resultado = resultado.text

        assert resultado == '15'


if __name__ == "__main__":
    pytest.main()
