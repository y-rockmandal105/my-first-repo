import os
from flask import Flask
from flask_executor import Executor
app = Flask(__name__)

executor = Executor(app)

@app.route("/")
def hello():
    return "Hey ! you are all done"

@app.route("/work")
def index():
    executor.submit(long_running_job)
    return "Doing a work"

def long_running_job():
    os.system("python work.py")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
