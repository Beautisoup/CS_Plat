# server.py
# 初始化 JWT

import argparse
from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_jwt_extended import JWTManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# 定义 app
app = Flask(__name__)
# 注册 restx，路由管理
api = Api(app)
# 解决跨域
CORS(app, supports_credentials=True)

# 注册 jwt
jwt = JWTManager(app)
# 配置服务端密钥
app.config["JWT_SECRET_KEY"] = "zidingyi"
# 开启数据库跟踪模式
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# SQLAlchemy 设置
Base = declarative_base()
# 定义数据库
db_host = "localhost"  # MySQL主机名
db_port = "3306"  # MySQL端口号，默认3306
db_name = "testplat"  # 数据库名称
db_user = "root"  # 数据库用户名
db_pass = "123456"  # 数据库密码
# 数据库类型+数据库引擎（ pip install pymysql）
db_url = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
# 创建引擎，连接到数据库
# engine = create_engine('sqlite:///data.db', echo=True)
engine = create_engine(db_url, echo=True)
# 创建session对象
DBSession = sessionmaker(bind=engine)
db_session: Session = DBSession()

# 注册路由
def register_router():
    from controller.testcase_controller import testcase_ns
    from controller.plan_controller import plan_ns
    from controller.record_controller import record_ns
    from controller.user_controller import user_ns

    api.add_namespace(testcase_ns, "/testcase")
    api.add_namespace(plan_ns, "/plan")
    api.add_namespace(record_ns, "/record")
    api.add_namespace(user_ns, "/user")


if __name__ == '__main__':
    # 注册路由
    register_router()
    # ArgumentParser() 解析命令行参数并生成帮助文档
    parser = argparse.ArgumentParser()
    # add_argument() 添加具体的命令行参数和对应的帮助信息
    parser.add_argument("--port", type=int, default=5055, help="服务启动端口")
    # 解析命令行参数并返回一个 Namespace 对象，该对象包含了所有解析出来的参数
    args = parser.parse_args()
    # 启动服务
    app.run(host="0.0.0.0", debug=True, port=args.port)
