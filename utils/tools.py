import json
import logging
import random
import time
from logging import handlers
from config import PATH


def read_json(file_name):
    """
    读取JSON文件并转换为格式为 [(), (), ...] 的列表
    :param file_name: json文件名
    :return: 列表
    """
    data = []  # 空列表
    file_path = PATH + "/data/" + file_name  # JSON文件路径
    # 打开JSON文件
    with open(file_path, mode='r', encoding='utf-8') as f:
        # 读取JSON文件并解析为Python对象【列表套字典】
        tmp = json.load(f)
        for i in tmp:
            a = tuple(i.values())
            data.append(a)
        # 返回列表
        return data

def gen_mobile():
    """生成随机手机号"""
    prefixes = ["130","131","132","133","134","135","136","137","138","139",
                "150","151","152","153","155","156","157","158","159",
                "170","171","172","173","175","176","177","178",
                "180","181","182","183","184","185","186","187","188","189"]
    prefix = random.choice(prefixes)
    # 用时间/随机数生成后 8 位（确保长度 11）
    suffix = str(int(time.time() * 1000))[-8:]
    return prefix + suffix

def gen_account(length=11):
    """生成指定长度的随机数字账号（首位非零）"""
    if length <= 0:
        return ""
    first = str(random.randint(1, 9))
    rest = ''.join([str(random.randint(0, 9)) for _ in range(length - 1)])
    return first + rest

class GetLog:
    """日志管理器（单例）"""
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 使用独立日志器，避免污染 root logger
            cls.__log = logging.getLogger("UITest")
            # 日志入口级别设为 DEBUG，各 Handler 自行过滤
            cls.__log.setLevel(logging.DEBUG)

            # 控制台处理器（INFO 及以上输出到控制台）
            sh = logging.StreamHandler()
            sh.setLevel(logging.INFO)
            fmt_console = "%(asctime)s %(levelname)s - %(message)s"
            sh.setFormatter(logging.Formatter(fmt_console))
            cls.__log.addHandler(sh)

            # 文件处理器（DEBUG 及以上写入文件，按天归档）
            filename = PATH + "/log/web.log"
            tf = handlers.TimedRotatingFileHandler(
                filename=filename,
                when="midnight",
                interval=1,
                backupCount=3,
                encoding="utf-8"
            )
            tf.setLevel(logging.DEBUG)
            fmt_file = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            tf.setFormatter(logging.Formatter(fmt_file))
            cls.__log.addHandler(tf)

        return cls.__log


