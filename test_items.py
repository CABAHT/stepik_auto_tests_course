from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

def test_add_in_cart_buuton_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(6)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")