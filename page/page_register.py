import time

from selenium.webdriver.common.by import By
from base.base import BasePage
from config import BASE_URL


class PageRegister(BasePage):


    def __init__(self,driver):
        """设置页面实例属性（元素定位）"""
        super().__init__(driver)
        # 页面元素定位
        self.accountsElement=(
            By.XPATH,
            "//input[@name='accounts']"
        )
        self.pwdElement=(
            By.XPATH,
            "//input[@name='pwd']"
        )
        self.agreement_checkboxElement = (
                By.XPATH,
                "/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[1]/form/div[4]/label/span/i[2]"
            )
        self.captcha_imgElement = (By.ID, "form-verify-img")
        self.captcha_inputElement = (By.XPATH, "//input[@name='verify']")
        self.register_buttonElement = (
            By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[1]/form/div[5]/button"
        )
        # 成功结果元素定位
        self.success_result =(By.XPATH, "//*[contains(text(), '欢迎来到')]")
        # 失败结果元素定位 #reg_form > div.reg-title
        self.fail_result = (By.XPATH, "//*[contains(text(), '欢迎注册')]")

    def open_url(self):
        """打开网页"""
        self.driver.get(BASE_URL + "/?s=user/regInfo.html")
    def register(self, accounts, pwd):
        # 输入手机号
        self.base_input(self.accountsElement, accounts)
        # 输入密码
        self.base_input(self.pwdElement, pwd)
        # 图片验证码
        shot = self.get_captcha_img(self.captcha_imgElement)
        # 输入图片验证码
        self.base_input(self.captcha_inputElement, shot)
        #点击 同意协议
        self.base_click(self.agreement_checkboxElement)
        # 点击 注册
        self.base_click(self.register_buttonElement)
        time.sleep(2)
    def get_captcha_img(self, loc):
        """获取图片验证码"""
        captcha_img = self.fd_element(loc)#定位图片验证码元素
        img_bytes = captcha_img.screenshot_as_png#获取图片字节码
        captcha_code = self.ocr.classification(img_bytes)#识别图片字节码，产出验证码
        return captcha_code

    def get_success_result(self):
        """获取注册成功信息"""
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        """获取注册失败信息"""
        return self.fd_element(self.fail_result).text