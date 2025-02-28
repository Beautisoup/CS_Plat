# 测试用例 Service
# service/testcase_service.py

from typing import List
from backend.dao.testcase_dao import TestcaseDao
from backend.model.testcase_model import TestcaseModel

# 实例化测试用例实体类
testcase_dao = TestcaseDao()


class TestcaseService:
    def create(self, testcase_model: TestcaseModel) -> int:
        """
        创建用例
        """
        result = testcase_dao.get_by_name(testcase_model.name)
        if not result:
            return testcase_dao.create(testcase_model)

    def update(self, testcase_model: TestcaseModel) -> int:
        """
        更新用例，以id为条件
        """
        # 根据 id 检查用例是否存在
        existing_testcase = testcase_dao.get(testcase_model.id)
        if existing_testcase:
            return testcase_dao.update(testcase_model)
        return 0  # 若用例不存在，返回 0 表示更新失败

    def delete(self, testcase_id: int) -> int:
        """
        删除用例
        """
        if self.get(testcase_id):
            return testcase_dao.delete(testcase_id)

    def list(self) -> List[TestcaseModel]:
        """
        获取全部用例
        """
        return testcase_dao.list()

    def get(self, testcase_id: int) -> TestcaseModel:
        """
        获取某个测试用例
        """
        return testcase_dao.get(testcase_id)