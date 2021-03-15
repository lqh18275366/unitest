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