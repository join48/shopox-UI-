# 项目配置相关的文件
import os
from faker import Faker
# 获取项目路径[不同操作系统都可以获取]
PATH = os.path.dirname(os.path.dirname(__file__))
# print(PATH)
# 项目的地址[切换测试环境]
BASE_URL = "http://localhost/"
BACK_URL = "http://121.43.169.97:8082"
# 人的信息
fk = Faker(locale="zh_CN")
# 姓名，手机号，身份证
NAME = fk.name()
PHONE = fk.phone_number()
CARD = fk.ssn()
# 浏览器驱动配置（可通过环境变量覆盖）
DRIVER_PATH = os.environ.get("WEBDRIVER_PATH", r"D:\Surface\Document\PyCharmMiscProject\chromedriver-win64\chromedriver.exe")
BROWSER_TYPE = os.environ.get("BROWSER_TYPE", "edge")

# print(NAME, PHONE, CARD)