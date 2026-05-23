import os
import ddddocr
from config import PATH
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from tools import GetLog

# 在模块级别设置环境变量，禁用ddddocr欢迎信息
os.environ['PYTHONWARNINGS'] = 'ignore'

class BasePage(object):

    def __init__(self, driver, timeout=10):
        # 获取浏览器对象
        self.driver = driver
        self.default_timeout = timeout  # 默认等待时间
        # 抑制ddddocr的欢迎信息
        import io
        from contextlib import redirect_stdout, redirect_stderr

        f = io.StringIO()
        with redirect_stdout(f), redirect_stderr(f):
            self.ocr = ddddocr.DdddOcr()  # 创建ocr对象

    def fd_element(self, loc):
        """
        元素定位的公共方法
        :param loc: 元素定位方式及属性值
        :return: 定位到的元素
        """
        try:
            # 推荐写法
            # 元素需要可见
            # element = WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(loc))
            # 元素可以不可见也能定位
            element = WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(loc))
            return element
        except Exception as e:
            GetLog.get_log().error(f"元素定位超时，定位信息：{loc}，错误详情：{e}")
            raise   # 重新抛出异常供上层处理

    def base_input(self, loc, text):
        """
        输入框输入公共方法
        :param loc: 元素定位方式及属性值
        :param text: 输入内容
        :return: 无
        """
        # 定位元素
        ele = self.fd_element(loc)
        # 清空输入框
        ele.clear()
        # 输入内容
        ele.send_keys(text)

    def base_click(self, loc):
        """
        点击公共方法
        :param loc: 元素定位方式及属性值
        :return: 无
        """
        self.fd_element(loc).click()

    def get_captcha_img(self,loc):
        """
        获取图片验证码
        :param loc: 元素定位信息
        :return: 图片验证码
        """
        captcha_img=self.fd_element(loc)#定位图片验证码元素

        img_bytes = captcha_img.screenshot_as_png#获取图片字节码
        captcha_code = self.ocr.classification(img_bytes)#识别图片字节码，产出验证码
        return captcha_code

    def mouse_move(self, loc):
        """
        鼠标移动
        :param loc: 元素定位信息
        :return: 无
        """
        ele = self.fd_element(loc)
        ActionChains(self.driver).move_to_element(ele).perform()

    def get_shot(self, file_name):
        """
        截图
        :param file_name: 截图文件名
        :return:无
        """
        # self.driver.get_screenshot_as_file(PATH + r"\img\pwd_error.png")
        # self.driver.get_screenshot_as_file(PATH + '/img/' + file_name)
        # 推荐
        file_path = os.path.join(PATH, 'img', file_name)
        self.driver.get_screenshot_as_file(file_path)

    def base_switch_handle(self, loc):
        """
        切换多窗口并获取指定元素
        :param loc: 定位的元素信息
        :return: 第二个窗口的页面元素
        """
        # 等待页面加载
        WebDriverWait(self.driver, self.default_timeout).until(lambda x: len(x.window_handles) > 1)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        # 切换到新窗口进行定位
        element = self.fd_element(loc)
        return element

    def base_switch_frame(self, loc):
        """
        切换frame
        :param loc: frame的定位信息
        :return: 无
        """
        frame_ele = self.fd_element(loc)
        self.driver.switch_to.frame(frame_ele)

    def base_default_frame(self):
        """
        切换到默认frame
        :return: 无
        """
        self.driver.switch_to.default_content()

    def base_select_list(self, loc, text):
        """
        下拉框选择
        :param loc: 元素定位信息
        :param text: 选择的文本
        :return: 无
        """
        ele = self.fd_element(loc)
        Select(ele).select_by_visible_text(text)
