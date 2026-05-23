# 类三要素
# 1.定义页面类
# 2.设置实例属性
# 3.定义实例方法
import time
from base.base import BasePage
from config import BASE_URL
from selenium.webdriver.common.by import By


class PageBuy(BasePage):
    """购买页面类"""

    def __init__(self, driver):
        """初始化方法"""
        super().__init__(driver)
        # 设置页面实例属性 - 优化命名和注释
        self.category_main = (By.CLASS_NAME, "span[value='时尚服饰']")
        self.category_sub = (By.XPATH, "//*[text()='男装']")
        self.product = (By.LINK_TEXT, "南极人（Nanjiren）裤子夏季男宽松休闲百搭裤华夫格长裤运动裤子潮流束脚裤休闲裤男")
        self.color = (By.CLASS_NAME, "span[value='粉色']")
        self.size = (By.CLASS_NAME, "span[value='S+S']")
        self.buy_button = (By.CLASS_NAME, "button[value='立即购买']")
        self.add_address = (By.CLASS_NAME, "button[value='添加新地址']")  # 修正拼写: adress -> address
        self.address_name = (By.CLASS_NAME, "input[name='name']")
        self.address_alias = (By.CLASS_NAME, "input[name='alias']")
        self.address_phone = (By.CLASS_NAME, "input[name='tel']")
        self.address_province = (By.XPATH, "/html/body/div[1]/div[1]/div/form/div[4]/div/div[1]/div[1]/span")
        self.address_city1 = (By.CLASS_NAME, "span[value='北京市']")
        self.address_city2 = (By.CLASS_NAME, "span[value='北京市']")
        self.address_district = (By.CLASS_NAME, "span[value='东城区']")
        self.address_street = (By.CLASS_NAME, "input[placeholder='地区编号']")
        self.address_detail = (By.CLASS_NAME, "input[name='address']")
        self.address_default = (By.XPATH, "/html/body/div[1]/div[1]/div/form/div[6]/div")
        self.address_save_button = (By.CLASS_NAME, "span[value='保存']")

    # 建议添加业务方法
    def select_category(self, main_category, sub_category=None):
        """选择商品分类"""
        self.base_click(self.category_main)
        if sub_category:
            self.base_click(self.category_sub)

    def select_product(self):
        """选择商品"""
        self.base_click(self.product)

    def select_specifications(self, color=None, size=None):
        """选择商品规格"""
        if color:
            self.base_click(self.color)
        if size:
            self.base_click(self.size)

    def click_buy(self):
        """点击立即购买"""
        self.base_click(self.buy_button)

    def fill_address(self, name, alias, phone, province="北京市", city="北京市",
                     district="东城区", street="", detail_address="", set_default=True):
        """填写收货地址"""
        self.base_click(self.add_address)
        self.base_input(self.address_name, name)
        self.base_input(self.address_alias, alias)
        self.base_input(self.address_phone, phone)
        # 这里可以继续完善地址填写逻辑

    def save_address(self):
        """保存地址"""
        self.base_click(self.address_save_button)

    def open_url(self):
        """打开网页"""
        self.driver.get(BASE_URL)





