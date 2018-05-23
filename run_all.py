import unittest
import HTMLTestRunner01
import time


now_time = time.strftime("%y-%m-%d %H.%M.%S")
case_all = "D:\\pythontest\\wookapp\\case"

discoverall = unittest.defaultTestLoader.discover(start_dir=case_all,
                                                 pattern="test*.py",
                                                 top_level_dir=None)

re = "D:\\pythontest\\wookapp\\report\\"+now_time+".html"
f = open(re,"wb")

r = HTMLTestRunner01.HTMLTestRunner(stream=f,
                                  title="测试报告",
                                  description="测试详情")

r.run(discoverall)

