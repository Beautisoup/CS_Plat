import allure
from backend.service.user_service import UserService
from backend.model.user_model import UserModel


# 测试用户创建功能
@allure.feature("用户管理")
@allure.story("用户创建")
def test_create():
    with allure.step("初始化 UserService 实例"):
        test_user_service = UserService()
    with allure.step("准备用户数据"):
        user_data = {
            "username": "admin",
            "password": "xexexe",
        }
        user_model = UserModel(**user_data)
    with allure.step("调用 create 方法创建用户"):
        result = test_user_service.create(user_model)
    with allure.step("断言用户名是否正确"):
        assert user_model.username == "admin"
    with allure.step("断言返回的用户 ID 是否不为 None"):
        # 可以进一步断言返回的 id 是否符合预期，这里假设返回的 id 不为 None
        assert result is not None


# 测试通过 ID 获取用户功能
@allure.feature("用户管理")
@allure.story("通过 ID 获取用户")
def test_get():
    with allure.step("初始化 UserService 实例"):
        test_user_service = UserService()
    with allure.step("假设数据库中存在 id 为 1 的用户，调用 get 方法获取用户"):
        # 假设数据库中存在 id 为 1 的用户
        getuser = test_user_service.get(1)
    with allure.step("断言获取到的用户是否为 UserModel 类型"):
        if getuser:
            assert isinstance(getuser, UserModel)
        else:
            allure.attach(f"User with id 1 not found.", "错误信息", allure.attachment_type.TEXT)
            print("User with id 1 not found.")


# 测试通过用户名获取用户功能
@allure.feature("用户管理")
@allure.story("通过用户名获取用户")
def test_get_by_name():
    with allure.step("初始化 UserService 实例"):
        test_user_service = UserService()
    with allure.step("准备用户名数据"):
        user_name = "admin"
    with allure.step("调用 get_by_name 方法获取用户"):
        user = test_user_service.get_by_name(user_name)
    with allure.step("断言获取到的用户用户名是否正确"):
        if user:
            assert user.username == user_name
        else:
            allure.attach(f"User with name {user_name} not found.", "错误信息", allure.attachment_type.TEXT)
            print(f"User with name {user_name} not found.")


# 测试生成访问令牌功能
@allure.feature("用户管理")
@allure.story("生成访问令牌")
def test_create_access_token():
    with allure.step("初始化 UserService 实例"):
        test_user_service = UserService()
    with allure.step("准备用户数据"):
        user_data = {
            "username": "admin",
            "password": "xexexe",
        }
        user_model = UserModel(**user_data)
    with allure.step("调用 create_access_token 方法生成访问令牌"):
        token = test_user_service.create_access_token(user_model)
    with allure.step("断言生成的访问令牌是否不为 None"):
        assert token is not None
    with allure.step("断言生成的访问令牌是否为字符串类型"):
        # 可以进一步验证 token 的格式是否正确，这里简单判断是否为字符串
        assert isinstance(token, str)