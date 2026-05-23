# 类三要素
# 1.定义页面类
# 2.设置实例属性
# 3.定义实例方法
import time
from base.base import BasePage
from config import BASE_URL
from tools import DriverTools
from selenium.webdriver.common.by import By


class PageLogin(BasePage):
    """登录页面类"""

    def __init__(self, driver):
        """初始化方法"""
        # 获取driver对象
        # self.driver = DriverTools.get_driver()
        super().__init__(driver)
        # 设置页面实例属性
        self.loginPATH = (By.LINK_TEXT, "登录")
        self.accountsPATH = (By.CSS_SELECTOR, "input[name='accounts']")
        self.passwordPATH = (By.CSS_SELECTOR, "form input[name='pwd']")
        self.captcha_imgPATH=(By.ID, "form-verify-img")
        self.captcha_inputPATH = (By.XPATH, "//input[@name='verify']")
        self.login_buttonPATH = (By.XPATH, "/html/body/div[1]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/form/div[4]/button")
        # 成功结果元素属性
        self.success_result = (By.CLASS_NAME,"em[value='您好']")
        # 失败结果元素属性 #err > span
        self.fail_result = (By.XPATH, "//*[contains(text(), '欢迎登录')]")

    def open_url(self):
        """打开网页"""
        self.driver.get(BASE_URL + "/?s=user/loginInfo.html")

    def login(self, accounts, password):
        """登录"""
        # 输入账号
        self.base_input(self.accountsPATH, accounts)
        # 输入密码
        self.base_input(self.passwordPATH, password)
        # 图片验证码
        shot = self.get_captcha_img(self.captcha_imgPATH)
        # 输入图片验证码
        self.base_input(self.captcha_inputPATH, shot)
        # 点击登录
        self.base_click(self.login_buttonPATH)
        time.sleep(2)

    def get_success_result(self):
        """获取成功结果"""
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        """获取失败结果"""
        return self.fd_element(self.fail_result).text


if __name__ == '__main__':
    # 创建对象
    lg = PageLogin(DriverTools.get_driver())
    # 打开页面
    lg.open_url()
    # 操作登录
    lg.login("18400099090","123456")
    print(lg.get_success_result())

