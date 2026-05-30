from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__, template_folder="templates", static_folder="static")

# 祝福列表
tips = [
    "大傻逼🙃",
    "要天天开心😆",
    "多喝沸水~😁",
    "顺顺利利",
    "梦想成真😆",
    "不知道写什么",
    "你是最棒的!!",
    "不要熬夜",
    "金榜题名",
    "新年快乐🧧",
    "臭傻逼🙃",
    "前程似锦",
    "心想事成",
    "早点休息",
    "新年快乐🧧",
    "新年快乐🧧",
    "新年快乐🧧"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/tips")
def get_tips():
    return jsonify(tips)

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)