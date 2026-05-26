import re
import pytest
from script import log
from utils.tools import read_json, gen_mobile, gen_account
from page.page_register import PageRegister


class TestRegister:

    @pytest.fixture(autouse=True)
    def setup(self, browser, request):
        """创建浏览器驱动（每个测试用例独立实例）"""
        self.driver = browser
        # 创建页面对象
        self.page = PageRegister(self.driver)
        # 打开页面
        self.page.open_url()
        yield
        # 截图
        title = getattr(self, 'current_title', 'unknown')
        method_name = request.function.__name__
        self.page.get_shot(f"{method_name}_{title}.png")

    @pytest.mark.parametrize("title,account,password,captcha_mode,skip_agreement,expect", read_json("register_fail.json"))
    def test_01_register_fail(self, title, account, password, captcha_mode, skip_agreement, expect):
        self.current_title = title
        # 注册
        self.page.register(account, password, captcha_mode, skip_agreement)
        # 获取失败结果
        result = self.page.get_fail_result()
        log.debug(f"测试用例：{title} | 注册结果: {result} | 期望值: {expect}")
        # 断言
        assert result in  expect

    @pytest.mark.parametrize("title,account,password,expect", read_json("register_seccess.json"))
    def test_02_register_success(self, title, account, password, expect):
        self.current_title = title
        if account == "AUTO_ACCOUNT":
            match = re.search(r'账号长度为(\d+)', title)
            if match:
                length = int(match.group(1))
                account = gen_account(length)
            else:
                account = gen_mobile()
        if password == "AUTO_ACCOUNT":
            match = re.search(r'密码长度为(\d+)', title)
            if match:
                length = int(match.group(1))
                password = gen_account(length)
            else:
                password = "1234567"
        self.page.register(account, password)
        result = self.page.get_success_result()
        log.debug(f"测试用例：{title} | 注册结果: {result} | 期望值: {expect}")
        assert result in  expect

