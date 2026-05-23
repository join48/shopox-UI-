import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import DRIVER_PATH, BROWSER_TYPE, PATH


def pytest_sessionstart(session):
    """测试会话开始前，清理上一次测试的截图"""
    img_dir = os.path.join(PATH, "img")
    if os.path.exists(img_dir):
        for filename in os.listdir(img_dir):
            file_path = os.path.join(img_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"清理截图文件失败: {file_path}, 错误: {e}")


@pytest.fixture(scope="function")
def browser():
    """创建浏览器驱动（每个测试用例独立实例）"""
    if BROWSER_TYPE == "chrome":
        if DRIVER_PATH:
            service = Service(executable_path=DRIVER_PATH)
            driver = webdriver.Chrome(service=service)
        else:
            driver = webdriver.Chrome()
    elif BROWSER_TYPE == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"不支持的浏览器类型: {BROWSER_TYPE}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


