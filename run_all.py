import unittest
from lib.HTMLTestReportCN import HTMLTestRunner  # 修改导入路径
from config.config import *  # 修改导入路径
from lib.send_email import send_email  # 修改导入路径

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover(test_path)  # 从配置文件中读取

with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述",tester="William").run(suite)

if send_email_after_run:  # 是否发送邮件
    send_email(report_file)
logging.info("================================== 测试结束 ==================================")
