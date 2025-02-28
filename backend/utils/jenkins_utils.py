"""

"""
from jenkinsapi.jenkins import Jenkins


class JenkinsUtils:
    # Jenkins 服务
    BASE_URL = "http://localhost:8083/"
    # Jenkins 服务对应的用户名
    USERNAME = "admin"
    # Jenkins 服务对应的token
    PASSWORD = "dd4f889c10164ec39a694432fb1ee583"
    # jenkins要操作的JOB名称
    JOB = "JenkinsTestLyr1"

    @classmethod
    def invoke(cls, invoke_params):
        #invoke_params,接收从测试计划哪来的参数
        """
        执行构建任务
        :return:
        """
        # 获取Jenkins对象
        jenkins_liyuanrui = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 获取Jenkins 的job 对象
        job = jenkins_liyuanrui.get_job(cls.JOB)
        # 构建 job， 传入的值必须是字典， key 对应 jenkins 设置的参数名
        # job.invoke(build_params={"task": "CalculatorProject/test/cases/test_div.py"})
        job.invoke(build_params={"methods": invoke_params})
        # 获取job 最后一次完成构建的编号
        # http://47.92.149.0:8080/job/ck24/20/allure/
        last_build_number = job.get_last_buildnumber()+1
        # pytest 用例名称 指定报告生成地址
        # pytest $task --alluredir=path
        report = f"{cls.BASE_URL}job/{cls.JOB}/{last_build_number}/allure/"
        return report