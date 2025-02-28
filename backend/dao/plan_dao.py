# 测试计划 Dao
# dao/plan_dao.py

from backend.model.plan_model import PlanModel
from backend.server import db_session


class PlanDao:

    def get(self, plan_id) -> PlanModel:
        # 根据id返回数据
        return db_session.query(PlanModel).filter_by(id=plan_id).first()

    def get_by_name(self, name) -> PlanModel:
        # 根据name返回数据
        return db_session.query(PlanModel).filter_by(name=name).first()

    def list(self):
        # 返回所有数据
        return db_session.query(PlanModel).all()

    def create(self, plan_do: PlanModel):
        # 新增数据
        db_session.add(plan_do)
        db_session.commit()
        return plan_do.id

    def delete(self, plan_id):
        # 删除操作
        db_session.query(PlanModel).filter_by(id=plan_id).delete()
        db_session.commit()
        return plan_id