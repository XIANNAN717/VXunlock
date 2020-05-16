# -*- coding: gb18030 -*-
# -*- coding: utf-8 -*-
from appium import webdriver

ServerUrl = 'http://127.0.0.1:4723/wd/hub'


def desired():
    desired_caps = {
        'noRest': True,  # ����APP����Ҫ���app���ԭ�е�����
        'platformName': 'Android',
        'platformVersion': '7.1',
        'unicodeKeyboard': True,  # ʹ��Unicode���뷨
        'resetKeyboard': True,  # �������뷨����ʼ״̬
        'deviceName': '843bd2f',
        # 'deviceName':'127.0.0.1:62001',
        'appPackage': 'com.upqing.sunflower',
        'appActivity': '.MainActivity'

    }
    driver = webdriver.Remote(ServerUrl, desired_caps)
    return driver


# ����
if __name__ == '__main__':
    des = desired()
