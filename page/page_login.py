# 类三要素
# 1.定义页面类
# 2.设置实例属性
# 3.定义实例方法
import time
from base.base import BasePage
from config import BASE_URL
from selenium.webdriver.common.by import By


class PageLogin(BasePage):
    """登录页面类"""

    def __init__(self, driver):
        """初始化方法"""
        # 获取driver对象
        super().__init__(driver)
        # 设置页面实例属性
        self.loginPATH = (By.LINK_TEXT, "登录")
        self.accountsPATH = (By.CSS_SELECTOR, "input[name='accounts']")
        self.passwordPATH = (By.CSS_SELECTOR, "form input[name='pwd']")
        self.login_buttonPATH = (By.XPATH, "/html/body/div[1]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/div/form/div[3]/button")
        # 成功结果元素属性
        self.success_result = (By.XPATH, "//*[contains(text(), '我的地址')]")
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
        # 点击登录
        self.base_click(self.login_buttonPATH)


    def get_success_result(self):
        """获取成功结果"""
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        """获取失败结果"""
        return self.fd_element(self.fail_result).text





