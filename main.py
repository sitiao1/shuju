# main.py
from flask import Flask
from routes.user_routes import register_routes


app = Flask(__name__, template_folder='templates')

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

# 注册所有路由
register_routes(app)

# 启动应用
if __name__ == '__main__':
    is_debug = False  # 可以根据需求修改
    if is_debug:
        app.run(host='127.0.0.1', port=5002, debug=True)
    else:
        app.run(host='60.205.59.6', port=8877, debug=False)
