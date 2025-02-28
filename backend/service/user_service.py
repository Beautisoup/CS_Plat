# 用户 Service
# service/user_service.py
from flask_jwt_extended import create_access_token
from backend.dao.user_dao import UserDao
from backend.model.user_model import UserModel
from backend.server import app,jwt
from backend.utils.log_util import logger
from datetime import timedelta
user_dao = UserDao()


class UserService:

    def get(self, user_id) -> UserModel:
        '''
        通过 ID 查询用户
        '''
        return user_dao.get(user_id)

    def get_by_name(self, user_name):
        '''
        通过姓名查询用户
        '''
        return user_dao.get_by_name(user_name)

    def create(self, user_model: UserModel) -> int:
        '''
        创建用户
        '''
        # 新增前先查询用户是否存在
        user = user_dao.get_by_name(user_model.username)
        if not user:
            # 没有重名，创建用户
            user_dao.create(user_model)
            return user_model.id

    def create_access_token(self, user_model):
        '''
        根据用户信息生成 token
        '''
        # 使用 jwt 生成 token
        with app.app_context():
            # token = create_access_token(identity=user_model.username, expires_delta=timedelta(days=1))
            # identity 是生成 token 的依据，需要 json 格式的可序列化数据
            # expires_delta 可以配置 token 的过期时间
            #create_access_token使用此方法要导入service的JWT
            token = create_access_token(
                identity=user_model.username,
                expires_delta=timedelta(days=1)
            )
            # 在 token 前拼接 Bearer 关键字
            return f'Bearer {token}'

    # 配置回调函数中验证数据条件/官方固定写法（使用create_access_token的官方固定写法）
    @jwt.user_lookup_loader
    def user_lookup_callback(self, _jwt_header, jwt_data):
        # 因为 sub 字段下是请求 body 的内容，所以从 sub 中获取用户名用来查库
        # 获取 username
        username = jwt_data["sub"]["username"]
        # 返回通过 username 查询用户的结果
        return self.get_by_name(username)