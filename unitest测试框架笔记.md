# 1  unitTest测试框架
python自带的单元测试框架，用于自动化测试解决后期的回归测试提高测试效率

## 1.1  unittest的属性
```
['BaseTestSuite', 'FunctionTestCase', 'SkipTest', 'TestCase', 'TestLoader', 'TestProgram', 'TestResult', 'TestSuite', 'TextTestResult', 'TextTestRunner', '_TextTestResult', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', '__unittest', 'case', 'defaultTestLoader', 'expectedFailure', 'findTestCases', 'getTestCaseNames', 'installHandler', 'loader', 'main', 'makeSuite', 'registerResult', 'removeHandler', 'removeResult', 'result', 'runner', 'signals', 'skip', 'skipIf', 'skipUnless', 'suite', 'util']
```
- 注；常用的unittest的属性
    - testcase：测试用例(管理测试用例)
    - testsuite：测试套件（测试策略，共有300条测试用例，仅执行120条测试用例）
    - testTextRunner:运行测试用例

## 1.2  测试用例:TestCase
TestCase类的实例，作为编写的测试类的基类，具体测试由具体的子类（就是我们写的测试类）实现。此类实现测试运行程序所需的接口，以使其能够驱动测试，以及测试代码可用于检查和报告各种失败的方法
- 所编写的测试用例，必须是一个类，而且必须继承TestCase类 。
- 每个测试方法，都是以test开头
- 编写测试类，建议以Test开头
- 编写的模块，建议小写test开头

### 1.2.1  TestCase类的属性
```
['__call__', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_addSkip', '_baseAssertEqual', '_classSetupFailed', '_deprecate', '_diffThreshold', '_formatMessage', '_getAssertEqualityFunc', '_truncateMessage', 'addCleanup', 'addTypeEqualityFunc', 'assertAlmostEqual', 'assertAlmostEquals', 'assertDictContainsSubset', 'assertDictEqual', 'assertEqual', 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone', 'assertIsNot', 'assertIsNotNone', 'assertItemsEqual', 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals', 'assertNotEqual', 'assertNotEquals', 'assertNotIn', 'assertNotIsInstance', 'assertNotRegexpMatches', 'assertRaises', 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual', 'assertSetEqual', 'assertTrue', 'assertTupleEqual', 'assert_', 'countTestCases', 'debug', 'defaultTestResult', 'doCleanups', 'fail', 'failIf', 'failIfAlmostEqual', 'failIfEqual', 'failUnless', 'failUnlessAlmostEqual', 'failUnlessEqual', 'failUnlessRaises', 'failureException', 'id', 'longMessage', 'maxDiff', 'run', 'setUp', 'setUpClass', 'shortDescription', 'skipTest', 'tearDown', 'tearDownClass']
```
### 1.2.2  检查并报告故障：断言方法
```python
import unittest
from test_login_01 import get_username,get_password
#1. 使用unitest中的Testcase类：
# 1）. 所编写的测试用例，必须是一个类，而且必须继承TestCase类 。
# 2）. 每个测试方法，都是以test开头
# 3）. 编写测试类，建议以Test开头
# 4）. 编写的模块，建议小写test开头

"""
注：比较预期结果与实际结果是否相等
    1. 使用unittest的比较方法：unitest.TestCase.assertEqual(a,b)
    2. 使用python的断言方法：assert
"""
#① . 定义登陆类，且继承unittest的TestCase类
class Test_Login(unittest.TestCase):
    #② . 登陆用户名测试用例
    def test_login_username(self):
        # 预期结果：自己登陆的账号
        expect_username = 'test01'
        # 实际结果：显示在页面上的账号
        acul1_username = get_username()
        #比较预期结果与实际结果是否相等
        #1. 使用unitest.TestCase.assertEqual(a,b)
        self.assertEqual(expect_username,acul1_username)
        #2. 使用python的断言assert
        assert acul1_username == expect_username
    #③ . 登陆的用户密码测试用例
    def test_login_password(self):
        # 预期结果：登陆的密码
        expect_password = 'test01'
        # 实际结果：显示在页面上的密码
        acut1_password = get_password()
        self.assertEqual(expect_password,acut1_password)
        # assert acut1_password == expect_password

#④ . 将单元测试模块变为可直接运行的测试脚本，使用TestLoader类来搜索在该模块中以“test”命名开头的测试用例并自动执行
unittest.main()
```
### 2.2.3  运行测试：初始化/清空方法
- **初始化方法：setUp() ** 
    - setUp()方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库连接并进行初始化。如测试用例需要登录web，可以先实例化浏览器。
- **清空方法：tearDown() ** 
    - tearDown()方法用于测试用例执行之后的善后工作。如关闭数据库连接。关闭浏览器
- **setUpClass() ：bool(x) is True** 
    - 整个类在运行前，先运行setupClass()
- **tearDownClass() ：bool(x) is False** 
    - 整个类在运行结束时，先运行tearDownClass()
    
```python
    #在类中定义unittest的初始化或清空方法
    #类的初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass：执行类之前调用1次")
    #类的清空方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass：执行类之后调用一次")
    #初始化用例
    def setUp(self) -> None:
        print("setUp：每次执行测试用例前执行")
    #清空方法
    def tearDown(self) -> None:
        print("tearDown：每次执行测试用例后执行")
```
## 1.3  测试套件:testsuite
将一组测试用例放到一起运行，放在一起的用例叫测试套件
### 1.3.1  TestSuite类的属性
```
['__call__', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_addClassOrModuleLevelException', '_get_previous_module', '_handleClassSetUp', '_handleModuleFixture', '_handleModuleTearDown', '_tearDownPreviousClass', '_tests', 'addTest', 'addTests', 'countTestCases', 'debug', 'run']
```

### 1.3.2  添加一条测试用例：addTest
```python
# 1）创建一个测试套件对象
suite = unittest.TestSuite()
# 2）添加一条测试用例:suite.addTest(类名('类方法'))
suite.addTest(Test_Login('test_login_username'))
suite.addTest(Test_Login('test_login_password'))
```
### 1.3.3  添加多条测试用例：addTests
```python
# 1）创建一个测试套件对象
suite = unittest.TestSuite()
# 2） 添加多条测试用例：addTests
lst = [Test_Login('test_login_username'),Test_Login('test_login_password')]
suite.addTests(lst)
```
### 1.3.4  自动搜索测试用例：TestLoader().discover()
```python
'''
suite = unittest.TestLoader().discover(test_dir, pattern='test*.py') 
自动搜索指定目录下指定开头的.py文件，并将查找到的测试用例组装到测试套件 
test_dir: 为指定的测试用例的目录 
pattern：为查找的.py文件的格式，
默认为'test*.py' 也可以使用unittest.defaultTestLoader 代替 unittest.TestLoader()
'''
#test_dir = '.':.为当前目录
suite = unittest.TestLoader().discover('.', pattern='test*.py')
```
## 1.4  运行所有测试用例（测试套件）
### 1.4.1  TextTextRunner的属性
run(suite)：运行测试套件，并收集结果信息传递给测试报告对象。
```
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_makeResult', 'buffer', 'descriptions', 'failfast', 'resultclass', 'run', 'stream', 'verbosity']
```
### 1.4.2  运行测试用例run（）
```python
#（1） 创建unittest.TextTestRunner()对象
runner = unittest.TextTestRunner()
#（2） 运行测试套件并收集结果信息传递给测试报告对象：run(suite)
runner.run(suite)
#（3） 运行结果将会提示一共运行几条测试用例，其中成功几条失败几条  F或 E 或 . 或S
#F:失败
#.:成功
#E:错误
#S：跳过
```

## 1.5  装饰器
### 1.5.1  不执行某测试用例或类：skip

对于一些未完成的或者不满足测试条件的测试函数和测试类，可以跳过执行

    - @unittest.skip(reason): skip(reason)装饰器：无条件跳过装饰的测试，并说明跳过测试的原因。
    
    - @unittest.skipIf(reason): skipIf(condition,reason)装饰器：条件为真时，跳过装饰的测试，并说明跳过测试的原因。
    
    - @unittest.skipUnless(reason): skipUnless(condition,reason)装饰器：条件为假时，跳过装饰的测试，并说明跳过测试的原因。
    
    - @unittest.expectedFailure(): expectedFailure()测试标记为失败。
#### 1.5.1.1  @unittest.skip('代码未完成')
```python
    #无条件跳过装饰的测试，并说明跳过测试的原因
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
```
#### 1.5.1.2  @unittest.skipIf(condition, reason)
```python
    #1.在类Test_Login(unittest.TestCase)外定义version=2
    #2.在方法test_login_username(self)前加入skip装饰器条件为真时，跳过装饰的测试，并说明跳过测试的原因
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
```
运行结果

![image-20210308234750605](C:\Users\李桥红\AppData\Roaming\Typora\typora-user-images\image-20210308234750605.png)

### 1.5.2  数据参数化（数据驱动）

```python
import unittest
from parameterized  import parameterized
#实现加法
def add(x,y):
    return x + y
test_data = [(1,1,2),(1,0,1),(-1,3,2)]
class TestAdd(unittest.TestCase):
    # # 方法1：定义三条测试用例，代码重复
    # def test_add_01(self):
    #     res1 = add(1,1)
    #     self.assertEqual(2,res1)
    #
    # def test_add_02(self):
    #     res2 = add(1,0)
    #     self.assertEqual(1,res2)
    # def test_add_03(self):
    #     res3 = add(-1,3)
    #     self.assertEqual(2,res3)

    # # 方法2：循环列表中3组数据，unittest运行结果执行1条测试用例，真实执行3组测试用例
    # def test_add(self):
    #     test_data = [(1,1,2),(1,1,0),(-1,3,2)]
    #     for x,y,expect_value in test_data:
    #         res = add(x,y)
    #         self.assertEqual(res,expect_value)

    # 方法3：数据参数化（数据驱动）:使用3组数据，unittest执行3条测试用例
    #1. 定义数据列表:test_data = [(1,1,2),(1,1,0),(-1,3,2)]
    #2. 使用参数化装饰器：parameterized
    @parameterized.expand(test_data)
    #3.定义测试用例
    def test_add(self,a,b,result):
        res = add(a,b)
        self.assertEqual(res,result)


if __name__ == '__main__':
    unittest.main()
```
## 生成html测试报告
生成html测试报告步骤
```
1. 复制HTMLTestRunner.py文件到项目文件夹
2. 导入HTMLTestRunner、unittest包
3. 生成测试套件
    suite = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
4. 设置报告生成路径和文件名
    file_name = "./test_report.html"
5. 打开报告
    with open(file_name,'wb') as f:
6. 实例化HTMLTestRunner对象：
    runner = HTMLTestRunner(stream=f,[title],[description])
    参数说明：
        stream：文件流，打开写入报告的名称及写入编码格式)
        title：[可选参数]，为报告标题，如XXX自动化测试报告
        description：[可选参数]，为报告描述信息；比如操作系统、浏览器等版本
7. 执行：runner.run(suite)
```
```python
import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover('.',pattern='test*.py')

# #方法1：使用unittest运行器运行测试套件
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 方法2：使用HTML_TestRunner去生成测试报告

    #（1） 生成测试报告文件
test_report = 'test_report.html'

    #（2） 打开上面的文件并将运行的结果写到文件中
with open(test_report,'wb') as f:
        # ① 创建一个HTMLTestRunner的，运行器
    runner = HTMLTestRunner(f,title='测试报告',description='当前版本：v1.0')
        # ② 调用run方法执行测试套件
    runner.run(suite)
```

# 2  附录

## 2.1  安装包

（1）安装git验证是否安装成功：git --version （安装方法：双击Git-2.22.0-64-bit.exe安装包）
（2）安装parameterized装饰器：pip install parameterized 

（3）安装postman——账号（用户名：lqh1222 密码：lqh072563）

（4）注册github账号——连接：https://github.com/——账号（用户名：lqh18275366 密码：lqh072563）

（5）java环境——安装（双击jdk-8u144-windows-x64.exe）——配置环境变量（C:\Program Files\Java\jdk1.8.0_144\bin 和 C:\ProgramData\Oracle\Java\javapath）——验证（java -version ）

（6）安装node——验证（node -v）

（7）安装loguru：pip install loguru——安装成功后的Version: 0.5.3

（8）更新pip包：python -m pip install --upgrade pip

（9）安装MicrosoftVCTools

