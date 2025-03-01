import os
import subprocess
import webbrowser
import shutil

def run_test():
    result = 'allure_results'
    if not os.path.exists(result):
        os.mkdir(result)
        # 清除旧的测试结果
    if os.path.exists(result):
        shutil.rmtree(result)
    os.mkdir(result)
    args_list = ['-s', '-v', 'test_user_service.py', '--alluredir', result]
    try:
        # 运行 pytest 测试
        subprocess.run(['pytest'] + args_list, check=True)
    except subprocess.CalledProcessError as e:
        print(f"运行测试时出现错误: {e}")

# 使用 allure serve 打开报告
def open_allure_report():
    report_dir = './allure_results'  # 报告目录
    cmd = f'allure serve {report_dir}'  # 使用 allure serve 打开报告
    subprocess.run(cmd, shell=True)  # 执行命令

if __name__ == '__main__':
    run_test()  # 运行测试
    open_allure_report()  # 生成 Allure 报告