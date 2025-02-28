# 测试用例 Dao
# dao/testcase_dao.py

"""
和数据库交互
"""
from backend.model.testcase_model import TestcaseModel
from backend.server import db_session


class TestcaseDao:

    def get(self, testcase_id: int) -> TestcaseModel:
        """
        添加用例
        :param testcase_id: 用例id
        :return: TestcaseModel
        """
        return db_session.query(TestcaseModel).filter_by(id=testcase_id).first()

    def get_by_name(self, testcase_name: str) -> TestcaseModel:
        """
        根据测试用例名称查询
        """
        return db_session.query(TestcaseModel).filter_by(name=testcase_name).first()

    def list(self):
        """
        获取用例列表
        :return:
        """
        return db_session.query(TestcaseModel).all()

    def create(self, testcase_model: TestcaseModel) -> int:
        """
        创建用例
        :param testcase_model: testcase对象
        :return:
        """
        db_session.add(testcase_model)
        db_session.commit()
        return testcase_model.id

    def delete(self, testcase_id: int) -> int:
        """
        删除用例
        :param testcase_id: 用例id
        :return:
        """
        db_session.query(TestcaseModel).filter_by(id=testcase_id).delete()
        db_session.commit()
        return testcase_id

    def update(self, testcase_model: TestcaseModel) -> int:
        """
        更新用例
        :param testcase_model: testcase对象
        :return:
        """
        try:
            db_session.query(TestcaseModel).filter_by(id=testcase_model.id).update(testcase_model.as_dict())
            db_session.commit()
            return testcase_model.id
        except Exception as e:
            db_session.rollback()  # 出现异常时回滚事务
            print(f"更新用例时出现错误: {e}")
            return 0  # 返回 0 表示更新失败