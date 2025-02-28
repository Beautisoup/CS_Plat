# """
# __author__ = '霍格沃兹测试开发学社'
# __desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
# """
# import requests
#
#
# from backend.service.plan_service import PlanService
# from backend.service.testcase_service import TestcaseService
#
# testcase_service = TestcaseService()
# plan_service = PlanService()
#
#
# def test_get():
#     testcase = testcase_service.get(1)
#     print(testcase)
#
#
# def test_list():
#     print(testcase_service.list())
#
#
# def test_case():
#     testcase1 = TestcaseDo(name="用例4", step="步骤4", method="方法4", remark="备注4")
#     # testcase1 = TestcaseDo(name="用例2", step="步骤2", method="方法2", remark="备注2")
#     testcase_id = testcase_service.save(testcase1)
#     print(testcase_id)
#     assert testcase_id
#
#
# def test_update():
#     testcase1 = TestcaseDo(id=1, name="用例11", step="步骤11", method="方法11", remark="备注11")
#     testcase_service.update(testcase1)
#     print(testcase_service.get(1).name)
#     assert testcase_service.get(1).name == "用例11"
#     assert testcase_service.get(1).step == "步骤11"
#     assert testcase_service.get(1).method == "方法11"
#     assert testcase_service.get(1).remark == "备注11"
#
#
# def test_delete():
#     testcase_service.delete(1)
#     print(testcase_service.get(1))
#     assert testcase_service.get(1) == None
#
#
# def test_get_by_name():
#     plan = testcase_service.get_by_name("用例4")
#     print(plan.as_dict())
#
# def test_get_c():
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTgxMjg2OCwianRpIjoiMGJmODJmODgtNTY4OC00ZjdmLWI3ZjgtYTZmNTc1NzM2NWU0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoicGJrZGYyOnNoYTI1NjoyNjAwMDAkZndpeHh3NnVueTF6QlNOYiQ3ZjcyMWE2NjU4MDBlYThhNWIzZDAxNWQ3YzkwN2RjOWJlOGQyMmRlNTA3NjJiNTI4ZWFjMTdjMjkyN2RkMDBhIiwicGhvbmUiOiIxMzMzMzMzMzMzMyIsImhlYWRfaW1nIjpudWxsLCJjcmVhdGVfdGltZSI6IjIwMjMtMDQtMTggMTc6Mzc6MjEifSwibmJmIjoxNjgxODEyODY4LCJleHAiOjE2ODE4MTM3Njh9.2kvr3ASLrMmunZti-V7Wobe6JP38v-tjrtK-RF9tqT0"
#     }
#     r = requests.get('http://127.0.0.1:5001/testcase', headers=headers)
#     print(r.json())
