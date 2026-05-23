import pytest
from script import log
from tools import read_json, gen_mobile
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

    @pytest.mark.parametrize("title,phone,password,expect", read_json("register_data.json"))
    def test_01_register_fail(self, title, phone, password, expect):
        self.current_title = title
        # 注册
        self.page.register(phone, password)
        # 获取失败结果
        result = self.page.get_fail_result()
        log.debug(f"测试用例：{title} | 注册结果: {result} | 期望值: {expect}")
        # 断言
        assert result in  expect

    @pytest.mark.parametrize("title,phone,password,expect", read_json("register_right.json"))
    def test_02_register_success(self, title, phone, password, expect):
        self.current_title = title
        if phone == "AUTO_PHONE":
            phone = gen_mobile()
        self.page.register(phone, password)
        result = self.page.get_success_result()
        log.debug(f"测试用例：{title} | 注册结果: {result} | 期望值: {expect}")
        assert result in  expect

