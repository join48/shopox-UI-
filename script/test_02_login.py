import pytest
from page.page_login import PageLogin
from script import log
from utils.tools import read_json


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, browser, request):
        self.driver = browser
        self.page = PageLogin(self.driver)
        self.page.open_url()
        yield
        title = getattr(self, 'current_title', 'unknown')
        method_name = request.function.__name__
        self.page.get_shot(f"{method_name}_{title}.png")

    @pytest.mark.parametrize("title,account,password,expect", read_json("login_success.json"))
    def test_01_login_scucess(self, title, account, password, expect):
        self.current_title = title
        self.page.login(account, password)
        result = self.page.get_success_result()
        log.debug(f"测试用例：{title} | 注册结果: {result} | 期望值: {expect}")
        assert  result in expect
    @pytest.mark.parametrize("title,account,password,expect", read_json("login_fail.json"))
    def test_02_login_fail(self, title, account, password, expect):
        self.current_title = title
        self.page.login(account, password)
        result = self.page.get_fail_result()
        log.debug(f"测试用例：{title} | 注册结果: {result} | 期望值: {expect}")
        assert result in expect
