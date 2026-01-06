from flask import Flask, render_template, request
import random

# 1. 初始化 Flask
app = Flask(__name__)

# ====================
# 2. 定義所有路由 (Routes)
# ====================

@app.route('/')
def home():
    user_name = "Chun"
    return render_template('bmi.html')

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    try:
        height_m = float(request.form['height']) / 100
        weight_kg = float(request.form['weight'])
        bmi = round(weight_kg / (height_m**2), 2)
        return render_template('bmi.html', bmi_result=bmi)
    except ValueError:
        return "❌ 請輸入正確的數字!"

@app.route('/about')
def about():
    return "<h2>我是 Chun，正在挑戰 7 天全端特訓!!</h2>"

# ====================
# 3. 啟動伺服器 (保護罩)
# ====================
if __name__ == '__main__':
    # 這行只會在你的電腦上執行，雲端 Gunicorn 會忽略它 (這是正確的)
    app.run(debug=True)