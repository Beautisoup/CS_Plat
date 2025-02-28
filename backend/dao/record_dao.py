# 测试记录 Dao
# dao/record_dao.py

from backend.model.record_model import RecordModel
from backend.server import db_session


class RecordDao:

    def list_by_plan_id(self, plan_id):
        # 根据id返回数据
        return db_session.query(RecordModel).filter_by(plan_id=plan_id).all()

    def list(self):
        # 返回所有数据
        return db_session.query(RecordModel).all()

    def create(self, build_do: RecordModel):
        # 新增数据
        db_session.add(build_do)
        db_session.commit()
        return build_do.id