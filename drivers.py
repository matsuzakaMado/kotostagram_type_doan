# -*- coding: utf-8 -*-
import platform

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Driver(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        # TODO cloud9で動かす場合はONにする
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--start-maximized')
        options.add_experimental_option('w3c', False)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-web-security')
        options.add_argument('--disable-desktop-notifications')
        options.add_argument('--disable-default-apps')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-infobars')
        options.add_argument('--test-type')
        options.add_argument('--log-level=2')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')

        if platform.system() != 'Windows':
            super().__init__(executable_path='./chromedriver', options=options)
        else:
            super().__init__(options=options)

    def login(self):
        raise NotImplementedError

    def search(self, keyword):
        raise NotImplementedError

    def follow(self):
        raise NotImplementedError

    def like(self):
        raise NotImplementedError

    def _wait_until(self, method, timeout=10):
        return WebDriverWait(self, timeout).until(method)
