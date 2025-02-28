# model/init_db.py

"""
初始化数据库表文件
"""
from backend.server import Base, engine
#在建表前要把所有表结构引入
from backend.model.plan_model import PlanModel
from backend.model.record_model import RecordModel
from backend.model.testcase_model import TestcaseModel
from backend.model.user_model import UserModel





if __name__ == '__main__':
    # 删除所有数据
    # Base.metadata.drop_all(bind=engine)
    # 创建表，需要传入创建连接的对象
    Base.metadata.create_all(bind=engine)