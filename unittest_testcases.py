import unittest
from selenium import webdriver
import time
from ddt import ddt, data, unpack, file_data

def readFile():
    params = []
    with open('params.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            params.append(line.strip().split(','))
    return params


@ddt
class AdvanceUsage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    @data('testng', 'unittest')
    def test_1(self, txt):
        self.driver.find_element_by_id('kw').send_keys(txt)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)

    def test_2(self):
        self.driver.find_element_by_id('kw').send_keys('cat')
        self.driver.find_element_by_id('su').click()

    @data('123', '456', '987')
    def test_3(self, text):
        print(text)
        print('***********')

    @data(('abc', 'efg'), ('xyz', '009'))
    def test_4(self, tup):
        print(tup)
        print('----------')

    @data(('cat', 'dog'), ('bad', 'good'))
    @unpack
    def test_5(self, tup1, tup2):
        print(tup1)
        print(tup2)
        print('-----*----')

    @data(*readFile())
    @unpack
    def test_6(self, url, word):
        self.driver.find_element_by_id('kw').send_keys(word)
        self.driver.find_element_by_id('su').click()

    @file_data('ppp.yml')
    def test_7(self, txt):
        print(txt)

    # 无条件跳过执行该用例
    @unittest.skip('无条件跳过执行该用例')
    def test_8(self):
        print('1 is executed.')

    # 条件为：如果为True则跳过
    @unittest.skipIf(1 < 2, '1 < 2 is False')
    def test_9(self):
        print('2 is executed.')

    # 条件为：除非怎么样，为False是跳过
    @unittest.skipUnless(1 < 2, '1 < 2 is False')
    def test_10(self):
        print('3 is executed.')

    # 如果用例执行失败，则不计入失败的case数中
    @unittest.expectedFailure
    def test_11(self):
        print('4 is executed.')
        self.assertEqual(4, 3, msg='notEqual')

    def test_12(self):
        print('4 is executed.')
        self.assertEqual(4, 3, msg='notEqual')

    @file_data('usage.yml')
    def test_13(self, **kwargs):
        name = kwargs.get('name')
        self.assertEqual(name, 'Oscar', msg='name different')
        text = kwargs.get('text')
        self.assertEqual(text, '666', msg='text different')
        print('**********')

"""
if __name__ == '__main__':
    # unittest.main(verbosity=2)
    # 创建一个测试套件 == list
    suite = unittest.TestSuite()

    # 添加测试用例（子元素）到测试套件（集合）
    suite.addTest(AdvanceUsage('test_1'))
    suite.addTest(AdvanceUsage('test_2'))
    suite.addTest(AdvanceUsage('test_3'))

    # 套件通过 TextTextTestRunner 对象运行 ≈ unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite)
"""
