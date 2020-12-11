# coding:utf-8
import pytest
from selenium import webdriver
# from selenium.webdriver.common.by import By
from time import sleep
import allure


@allure.title('登录测试')
@allure.feature('验证登录失败功能')
class Test_Login:

    @allure.step('登录操作')
    def webLogin(self, user, pwd):
        # driver = webdriver.Chrome()
        """
        解决chrome浏览器访问https时出现的安全验证的界面。
        普通启动方式：
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(chrome_options=options)
        """
        """
        Headless方式启动(无页面启动)
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://192.168.0.97')
        if user:
            driver.find_element_by_name('username').send_keys(user)
        if pwd:
            driver.find_element_by_name('password').send_keys(pwd)
        driver.find_element_by_xpath('//input[@value="Login"]').click()
        sleep(0.5)
        msg = driver.find_element_by_id('msg').text
        contact = driver.find_element_by_id('contact').text
        driver.quit()
        return msg, contact

    @pytest.mark.webtest
    @pytest.mark.parametrize(
        "user, pwd, msg_expected, contact_expected",
        [
            ('', '123456', 'Please input Username.', 'Contacts: Oscar'),
            ('oscar', '', 'Please input Password.', 'Contacts: Oscar'),
            ('oscar1', '1234', '-----------', '==========='),
            ('', '', 'Please input Username.', 'Contacts: Oscar (oxu@fortinet.com)'),
        ]
    )
    @allure.story('登录失败的用例')
    def test_login_wrong(self, user, pwd, msg_expected, contact_expected):
        msg, contact = self.webLogin(user=user, pwd=pwd)
        # if msg == msg_expected and contact == contact_expected:
        assert msg == msg_expected, "[msg expect]" + msg_expected + "; [actually]" + msg
        assert contact == contact_expected, "[contact expect]：" + contact_expected + "; [actually]" + contact


if __name__ == '__main__':
    # pytest.main(['-v', 'test_cases.py::Test_Login::test_login_wrong'])

    # 生成基于pytest-html的测试报告html文件
    # pytest.main(['-v', '--html=report.html'])

    # 生成 allure 测试报告html文件
    # allure generate ./allure_raw/ -o ./allure_report/ --clean
    # 生成 trend history 表数据：将旧数据 allure_report/history/ 目录复制到新数据的目录下。再运行 allure generate ...
    pytest.main(['-s', '-q', '--alluredir=allure_raw'])
