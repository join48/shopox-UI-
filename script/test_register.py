import pytest
from script import log
from tools import DriverTools, GetLog, read_json, gen_mobile

from page.page_register import PageRegister
from tools import DriverTools


class TestRegister:
    def setup_method(self):
        # 创建浏览器驱动对象
        self.driver = DriverTools.get_driver()
        # 创建页面对象
        self.page = PageRegister(self.driver)
        # 打开注册页面
        self.page.open_url()

    @pytest.mark.parametrize("title", read_json("register_data.json"))
    def teardown_method(self, title):
        # 截图
        self.page.get_shot(f"{title}.png")
        # 退出浏览器
        DriverTools.quit_driver()

    @pytest.mark.parametrize("title,phone,password,expect", read_json("register_data.json"))
    def test_01_register_fail(self, title, phone, password, expect):
        try:
            # 调用注册方法
            self.page.register(phone, password)
            # 获取注册结果
            result = self.page.get_fail_result()
            # 打印日志
            log.debug(f"测试用例：{title} | 注册结果: {result} | 期望值: {expect}")
            # 断言
            assert expect in result
        except Exception as e:
            log.error(f"测试执行过程中发生异常: {e}")
            raise

    @pytest.mark.parametrize("title,phone,password,expect", read_json("register_right.json"))
    def test_02_register_success(self, title,phone, password, expect):
        try:
            if phone == "AUTO_PHONE" or "{{unique}}" in phone:
                phone = gen_mobile()
            # 调用注册方法
            self.page.register(phone, password)
            # 获取注册结果
            result = self.page.get_success_result()
            # 打印日志
            log.debug(f"测试用例：{title} | 注册结果: {result} | 期望值: {expect}")
            # 断言
            assert expect in result
        except Exception as e:
            log.error(f"测试执行过程中发生异常: {e}")
            raise

