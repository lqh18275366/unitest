import unittest
from test_login_01 import get_username,get_password
#1. 使用unittest中的Testcase类：
# 1）. 所编写的测试用例，必须是一个类，而且必须继承TestCase类 。
# 2）. 每个测试方法，都是以test开头
# 3）. 编写测试类，建议以Test开头
# 4）. 编写的模块，建议小写test开头

"""
    比较预期结果与实际结果是否相等
        1. 使用unittest的比较方法：unitest.TestCase.assertEqual(a,b)
        2. 使用python的断言方法：assert
"""
version = 2.0
#① . 定义登陆类，且继承unittest的TestCase类
class Test_Login(unittest.TestCase):
    #类的初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass：类-前")
    #类的清空方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass：类-后")
    #初始化用例
    def setUp(self) -> None:
        print("setUp：方法-前")
    #清空方法
    def tearDown(self) -> None:
        print("tearDown：方法-后")
    #1.在类Test_Login(unittest.TestCase)外定义version=2
    #2.在方法test_login_username(self)将入skip装饰器条件为真不执行测试用例，反之则执行测试用例
    @unittest.skipIf(version>1, 'version>1不执行登陆用户名测试')
    #② . 登陆用户名测试用例
    def test_login_username(self):
        print("登陆用户名测试用例")
        # 预期结果：自己登陆的账号
        expect_username = 'test01'
        # 实际结果：显示在页面上的账号
        acul1_username = get_username()
        #比较预期结果与实际结果是否相等
        #1. 使用unitest.TestCase.assertEqual(a,b)
        self.assertEqual(expect_username,acul1_username)
        #2. 使用python的断言assert
        assert acul1_username == expect_username

    #对于一些未完成的或者不满足测试条件的测试函数和测试类，可以跳过执行
    #使用格式；@unittest.skipIf(condition, reason)
    @unittest.skip('跳过执行登陆密码测试用例')
    #③ . 登陆的用户密码测试用例
    def test_login_password(self):
        print("登陆密码测试用例")
        # 预期结果：登陆的密码
        expect_password = 'test01'
        # 实际结果：显示在页面上的密码
        acut1_password = get_password()
        self.assertEqual(expect_password,acut1_password)
        # assert acut1_password == expect_password
# #④ . 将单元测试模块变为可直接运行的测试脚本，使用TestLoader类来搜索在该模块中以“test”命名开头的测试用例并自动执行
# unittest.main()



#2. 使用unittest中的TestSuite去添加测试用例组成一组测试用例集合
# 1）创建一个测试套件对象
suite = unittest.TestSuite()

#2） 添加测试用例
#① 添加一条测试用例:suite.addTest(类名('类方法'))
suite.addTest(Test_Login('test_login_username'))
suite.addTest(Test_Login('test_login_password'))

# #② 添加多条测试用例：addTests
# lst = [Test_Login('test_login_username'),Test_Login('test_login_password')]
# suite.addTests(lst)

#③ TestLoader类：unittest.TestLoader().discover()
'''
suite = unittest.TestLoader().discover(test_dir, pattern='test*.py') 
自动搜索指定目录下指定开头的.py文件，并将查找到的测试用例组装到测试套件 
test_dir: 为指定的测试用例的目录 
pattern：为查找的.py文件的格式，
默认为'test*.py' 也可以使用unittest.defaultTestLoader 代替 unittest.TestLoader()
'''
# #test_dir = '.':.为当前目录
# suite = unittest.TestLoader().discover('.', pattern='test*.py')


# 3. TestTextRunner：运行测试用例
#（1）创建unittest.TextTestRunner()对象
runner = unittest.TextTestRunner()
#（2）运行测试套件并收集结果信息传递给测试报告对象：run(suite)
runner.run(suite)

#（3） 运行结果将会提示一共运行几条测试用例，其中成功几条失败几条  F或 E 或 . 或S
#F:失败
#.:成功
#E:错误
#S：跳过
