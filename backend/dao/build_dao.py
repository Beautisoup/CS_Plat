# 用户 Dao
# dao/user_dao.py

from model.user_model import UserModel
from server import db_session


class UserDao:

    def get(self, user_id) -> UserModel:
        '''
        根据 ID 查询用户
        '''
        return db_session.query(UserModel).filter_by(id=user_id).first()

    def get_by_name(self, user_name) -> UserModel:
        '''
        根据姓名查询用户
        '''
        return db_session.query(UserModel).filter_by(username=user_name).first()

    def create(self, user_model: UserModel):
        '''
        创建用户
        '''
        db_session.add(user_model)
        db_session.commit()
        return user_model.id