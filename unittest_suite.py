# coding:utf-8
import unittest
from CaseAdvanced_usage import *
import os
from HTMLTestRunner import HTMLTestRunner
from sendEmail import send_mail

# 创建一个测试套件 -> list
suite = unittest.TestSuite()
# print(suite)
# 第一种定义suite方式：添加测试用例（子元素）到测试套件（集合）
# suite.addTest(AdvanceUsage('test_1'))
# suite.addTest(AdvanceUsage('test_2'))
# suite.addTest(AdvanceUsage('test_3'))
# suite.addTest(AdvanceUsage('test_4'))

# 第二种定义suite方式：列表添加方法
# case = [
#     AdvanceUsage('test_1'),
#     AdvanceUsage('test_2'),
#     AdvanceUsage('test_3'),
#     AdvanceUsage('test_4')
# ]
# suite.addTests(case)

# 第三种：在指定的目录下批量运行case。
# test_dir = './'
# suite = unittest.defaultTestLoader.discover(
#     start_dir=test_dir,
#     pattern='CaseA*.py',
# )

# 第四种：添加文件名或类名。调用类名的方法用的比较多
# suite.addTests(unittest.TestLoader().loadTestsFromName('./CaseAdvanced_usage'))
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AdvanceUsage))

report_name = 'Test Report Name'
report_title = 'Test Report Title'
report_description = 'Test Report Description'
report_path = 'Report/'
report_file = report_path + 'report.html'
if not os.path.exists(report_path):
    os.mkdir(report_path)

with open(report_file, 'wb') as report:
    suite.addTests(unittest.TestLoader().loadTestsFromName('CaseAdvanced_usage'))
    # 如果套件结果HTMLTestRunner使用，则需要调用HTMLTestRunner中的运行器
    runner = HTMLTestRunner(
        stream=report,
        title=report_title,
        description=report_description
    )
    runner.run(suite)

send_mail(report_file)

# 套件通过 TextTextTestRunner 对象运行 ≈ unittest.main()
# runner = unittest.TextTestRunner()
# runner.run(suite)
