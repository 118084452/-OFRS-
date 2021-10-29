# coding:utf-8
import unittest
import os
import HTMLTestRunner
import datetime


# 用例路径
case_path = r"E:\python-test\unitest_frome"
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="case*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    time_stamp = datetime.datetime.now()
    time1 = time_stamp.strftime('%Y.%m.%d_%H.%M.%S')
    # html报告文件路径
    report_abspath = os.path.join(report_path, "result.html")
    report_abspath1 = '.{}.result.html'.format(time1)
    with open(report_abspath, "wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=u'自动化测试报告,测试结果如下：',
                                               description=u'用例执行情况：')
        # 调用add_case函数返回值
        runner.run(all_case())