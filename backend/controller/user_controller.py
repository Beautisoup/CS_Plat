# 用户管理接口
# controller/user_controller.py

from flask import request
from flask_restx import Namespace, Resource, fields
from backend.model.user_model import UserModel
from backend.server import db_session
from backend.service.user_service import UserService

# 定义用户管理的命名空间
# 可以在 Swagger 页面中为把用户管理相关接口放到一个组中管理
user_ns = Namespace("user", description="用户管理")

user_service = UserService()


# 定义路由
@user_ns.route("/login")
class LoginController(Resource):

    # post 接口请求体注解，会展示在 Swagger 页面中
    login_post_model = user_ns.model("login_post_model", {
        "username": fields.String,
        "password": fields.String
    })

    # 为接口添加设置好的注解
    @user_ns.expect(login_post_model)
    def post(self):
        '''
        登录功能
        '''

        # 检查会话状态
        if db_session.in_transaction() and db_session.is_active:
            try:
                # 尝试提交会话
                db_session.commit()
            except Exception as e:
                # 如果提交失败，回滚会话
                db_session.rollback()
        # 重置会话
        db_session.expunge_all()

        # 获取请求体
        data = request.json
        # 构建用户对象
        user = UserModel(**data)
        # 通过用户名查找用户是否存在
        user_result = user_service.get_by_name(user.username)
        # print(user_result)
        # print(data.get("password"))
        # 如果用户不存在，说明用户还未注册
        if not user_result:
            return {"code": 40013, "msg": "user is not register"},400
        # 如果密码不匹配，说明密码错误
        if not user_result.check_hash_password(data.get("password")):
            return {"code": 40014, "msg": "password is wrong"},400
        # 用户存在，且密码匹配，则生成 token
        access_token = user_service.create_access_token(user_result)
        # print(access_token)
        if access_token:
            # 存在access_token,则证明登录成功了
            return {"code": 0, "msg": "login success ", "data": {"token": access_token}}
        else:
            return {"code": 40021, "msg": "login fail"},400


@user_ns.route("/register")
class RegisterController(Resource):
    register_post_model = user_ns.model("register_post_model", {
        "username": fields.String,
        "password": fields.String
    })

    @user_ns.expect(register_post_model)
    def post(self):
        '''
        注册功能
        '''
        # 获取请求体
        data = request.json
        # 构建用户对象
        user = UserModel(**data)
        print(user.password)
        if user:
            user_id = user_service.create(user)
            if user_id:
                # 存在id,则证明新增成功了
                return {"code": 0, "msg": f"register success"},200
            else:
                return {"code": 40001, "msg": "register fail"},40001
        return {"code": 40001, "msg": "register fail"},40001