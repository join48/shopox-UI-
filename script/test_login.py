from page.page_login import PageLogin
from script import log
from tools import DriverTools, GetLog


class TestRegister:
    def setup_method(self):
        self.driver = DriverTools.get_driver()
        self.page = PageLogin(self.driver)
        self.page.open_url()

    def teardown_method(self):
        self.page.get_shot("back_login.png")
        DriverTools.quit_driver()

    def test_01_login_fail_phone_exist(self):
        try:
            self.phone = "1840009909"
            self.psw = "123456"
            self.page.login(self.phone, self.psw)

            result = self.page.get_fail_result()
            log.info(f"登录结果：{result}")
            assert "欢迎登录" in result
        except Exception as e:
            log.error(f"测试执行过程中发生异常: {e}")
            raise
