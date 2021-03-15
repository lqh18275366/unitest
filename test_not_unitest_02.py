
from test_login_01 import get_username,get_password


def test_login_username():
    #预期结果：自己登陆的账号
    expect_username = 'test01'
    #实际结果：显示在页面上的账号
    acul1_username = get_username()
    assert acul1_username == expect_username

def test_login_password():
    #预期结果：登陆的密码
    expect_password = 'test01'
    #实际结果：显示在页面上的密码
    acut1_password = get_password()
    assert acut1_password == expect_password
#不使用unitest测试框架执行测试用例
test_login_password()
test_login_username()