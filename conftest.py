import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page.page_login import PageLogin


# 编写浏览器驱动创建退出
@pytest.fixture()
def browser():
    # 创建浏览器驱动对象
    path = r"C:\Program Files\Python311\chromedriver.exe"
    ser = Service(executable_path=path)  # Chrome浏览器驱动服务对象
    driver = webdriver.Chrome(service=ser)  # 打开Chrome浏览器
    # 浏览器最大化
    driver.maximize_window()
    driver.implicitly_wait(10)
    # 返回驱动对象
    yield driver
    driver.quit()


