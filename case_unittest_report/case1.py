#coding=utf-8
import unittest
import requests

class DemoTest(unittest.TestCase):
    status = 200
    def setUp(self):
        self.url = 'https://www.baidu.com/'

    @unittest.skip("无条件跳过该测试")
    def test_blog1(self):
        # 无条件跳过
        """无条件跳过该测试"""
        r1 = requests.get(self.url)

    @unittest.skipIf(status > 400, "状态码大于200，就跳过该测试")
    def test_blog2(self):
        # 如果断言结果为真，则继续执行，否则跳过测试
        """如果断言结果为真，则继续执行，否则跳过测试"""
        r2 = requests.get(self.url)
        status2 = r2.status_code
        self.assertTrue(status2 > self.status)

    @unittest.skipUnless(status == 200, "状态码为200，则跳过")
    def test_blog3(self):
        # 除非结果为真，否则跳过该测试
        """除非结果为真，否则跳过该测试"""
        r3 = requests.get(self.url)
        status3 = r3.status_code
        self.assertTrue(status3 > self.status)

    @unittest.expectedFailure
    def test_blog4(self):
        # 将测试用例标记为“预期失败”，如果测试执行时失败，则测试结果不计为失败
        """将测试用例标记为“预期失败”，如果测试执行时失败，则测试结果不计为失败"""
        r4 = requests.get(self.url+'/test4')
        status4 = r4.status_code
        self.assertTrue(status4 == self.status)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()