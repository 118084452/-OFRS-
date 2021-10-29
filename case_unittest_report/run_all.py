#coding = utf-8
import unittest
import BeautifulReport as br
import datetime


class ZNTestRunner(object):
    def run(self):
        time_stamp = datetime.datetime.now()
        time1 = time_stamp.strftime('%Y.%m.%d_%H.%M.%S')
        test_suite = unittest.TestSuite()
        all_case = unittest.defaultTestLoader.discover('case', '*.py')
        [test_suite.addTests(case)for case in all_case]
        print(test_suite)
        report = br.BeautifulReport(test_suite)
        report.report(description='测试用例', filename='{}.html'.format(time1))


if __name__ == '__main__':
    aa = ZNTestRunner()
    aa.run()