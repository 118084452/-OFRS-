#coding=utf-8
import HTMLTestRunner
import BeautifulReport
import unittest
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有之前运行")
    @classmethod
    def tearDownClass(cls):
        print("所有之后运行")
    def setUp(self):
        print("之前运行")
    def tearDown(self):
        print("之后运行")
    def test_calc1(self):
        '''这是测试报告1'''
        print("这是case1")
    def test_calc2(self):
        '''这是测试报告2'''
        print("这是case2")