import time

from selenium.webdriver.common.by import By
from base.base import BasePage
from config import BASE_URL


class PageRegister(BasePage):


    def __init__(self,driver):
        """设置页面实例属性（元素定位）"""
        super().__init__(driver)
        # 页面元素定位
        self.accountsPath=(
            By.XPATH,
            "//input[@name='accounts']"
        )
        self.pwdPath=(
            By.XPATH,
            "//input[@name='pwd']"
        )
        self.agreement_checkboxPath = (
                By.XPATH,
                "/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[1]/form/div[4]/label/span/i[2]"
            )
        self.captcha_imgPath = (By.ID, "form-verify-img")
        self.captcha_inputPath = (By.XPATH, "//input[@name='verify']")
        self.register_buttonPath= (
            By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[1]/form/div[5]/button"
        )
        # 成功结果元素定位
        self.success_result =(By.XPATH, "//*[contains(text(), '，欢迎来到')]")
        # 失败结果元素定位 #reg_form > div.reg-title
        self.fail_result = (By.XPATH, "//*[contains(text(), '欢迎注册')]")

    def open_url(self):
        """打开网页"""
        self.driver.get(BASE_URL + "/?s=user/regInfo.html")


    def accounts(self, accounts):
        """输入手机号"""
        self.base_input(self.accountsPath, accounts)
    def pwd(self, pwd):
        """输入密码"""
        self.base_input(self.pwdPath, pwd)
    def captcha(self):
        # 图片验证码
        shot = self.get_captcha_img(self.captcha_imgPath)
        # 输入图片验证码
        self.base_input(self.captcha_inputPath, shot)
    def agrement(self):
        # 点击 同意协议
        self.base_click(self.agreement_checkboxPath)
    def register_button(self):
        """点击 注册"""
        self.base_click(self.register_buttonPath)
    def register(self, accounts, pwd, captcha_mode="input", skip_agreement=False):
        # 输入账号
        self.accounts(accounts)
        # 输入密码
        self.pwd(pwd)
        # 图片验证码：input=正常识别填写, skip=不填, error=填错误值
        if captcha_mode == "input":
            self.captcha()
        elif captcha_mode == "error":
            self.base_input(self.captcha_inputPath, "9999")
        # 点击 同意协议（可跳过）
        if skip_agreement is False:
            self.agrement()
        # 点击 注册
        self.register_button ()



    def get_success_result(self):
        """获取注册成功信息"""
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        """获取注册失败信息"""
        return self.fd_element(self.fail_result).text