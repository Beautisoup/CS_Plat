# 测试用例管理接口
# controller/testcase_controller.py

from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields
from backend.model.testcase_model import TestcaseModel
from backend.server import api
from backend.service.testcase_service import TestcaseService

# 定义测试用例的命名空间
# 可以在 Swagger 页面中为把测试用例管理相关接口放到一个组中管理
testcase_ns = Namespace("testcase", description="测试用例管理")

testcase_service = TestcaseService()


# 定义路由
@testcase_ns.route("")
class TestcaseController(Resource):
    # 鉴权操作
    decorators = [jwt_required()]

    # 测试用例管理 get 接口请求参数注解
    testcase_get_parser = api.parser()
    testcase_get_parser.add_argument("id", type=int, location="args")
    testcase_get_parser.add_argument('Authorization', type=str, location="headers")

    # 为 get 接口填写设置好的注解
    @testcase_ns.expect(testcase_get_parser)
    def get(self):
        '''
        测试用例查找
        '''
        # 获取请求参数
        data = request.args
        case_id = data.get("id")
        # 如果有id则进行数据查找
        if case_id:
            testcase = testcase_service.get(int(case_id))
            # 如果查询到结果
            if testcase:
                datas = [testcase.as_dict()]
                return {"code": 0, "msg": "get data success", "data": datas},200
            else:
                # 如果没有数据，则返回数据已存在
                return {"code": 40004, "msg": "data is not exists"},40004
        else:
            # 如果没有id,则返回全部数据
            datas = [testcase.as_dict() for testcase in testcase_service.list()]
            return {"code": 0, "msg": "get data success", "data": datas},200

    # 测试用例管理 post 接口请求体注解
    testcase_post_model = testcase_ns.model("testcase_post_model", {
        "name": fields.String,
        "step": fields.String,
        "method": fields.String,
        "remark": fields.String
    })
    # 测试用例管理 post 接口请求参数注解
    testcase_post_parser = api.parser()
    testcase_post_parser.add_argument('Authorization', type=str, location="headers")

    @testcase_ns.expect(testcase_post_model, testcase_post_parser)
    def post(self):
        '''
        新增测试用例
        '''
        # 获取请求体
        data = request.json
        # 构造测试用例对象
        testcase = TestcaseModel(**data)
        # 新增用例
        case_id = testcase_service.create(testcase)

        if case_id:
            # 存在测试用例id, 则证明用例新增成功了
            return {"code": 0, "msg": "add testcase success", "data": {"testcase_id": case_id}},200
        else:
            return {"code": 40001, "msg": "testcase is exists"},40001

    # 测试用例管理 put 接口请求体注解
    testcase_put_model = testcase_ns.model("testcase_put_model", {
        "id": fields.Integer,
        "name": fields.String,
        "step": fields.String,
        "method": fields.String,
        "remark": fields.String
    })
    # 测试用例管理 put 接口请求参数注解
    testcase_put_parser = api.parser()
    testcase_put_parser.add_argument('Authorization', type=str, location="headers")

    @testcase_ns.expect(testcase_put_model, testcase_put_parser)
    def put(self):
        '''
        更新测试用例
        '''
        try:
            # 获取请求体
            data = request.json
            # 构造测试用例对象
            testcase = TestcaseModel(**data)
            # 修改测试用例
            case_id = testcase_service.update(testcase)
            if case_id:
                # 存在测试用例id, 则证明用例更新成功了
                return {"code": 0, "msg": "update testcase success", "data": {"testcase_id": case_id}}
            else:
                return {"code": 40001, "msg": "update testcase fail"}
        except Exception as e:
            # 捕获异常并返回错误信息
            return {"code": 500, "msg": f"Internal server error: {str(e)}"}, 500

    # 测试用例管理 delete 接口请求参数注解
    testcase_delete_parser = api.parser()
    testcase_delete_parser.add_argument("id", type=int, location="json", required=True)
    testcase_delete_parser.add_argument('Authorization', type=str, location="headers")

    @testcase_ns.expect(testcase_delete_parser)
    def delete(self):
        '''
        删除测试用例
        '''
        # 获取请求体
        data = request.json
        delete_case_id = data.get("id")
        if delete_case_id:
            case_id = testcase_service.delete(delete_case_id)
            if case_id:
                # 存在测试用例id,则证明用例修改成功了
                return {"code": 0, "msg": f"delete testcase success", "data": {"testcase_id": case_id}}
            else:
                return {"code": 40001, "msg": "delete case fail"}