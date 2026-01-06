from flask import Flask, render_template, request
import random

# 1. 初始化 Flask 應用程式
app = Flask(__name__)

# 2. 定義路由 (首頁)
@app.route('/')
def home():
    # 這裡就是 Python 的邏輯層
    user_name = "Chun"
    number = random.randint(1, 100)  # 產生亂數
    # render_template 會把 HTML 讀進來，並把變數塞進 {{}} 裡面
    return render_template('bmi.html')

# 3. 計算路由 : 只接受 POST (表單送出)
@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    # 從網頁抓資料
    h_str = request.form['height']
    w_str = request.form['weight']

    # 進行運算
    try:
        height_m = float(h_str) / 100  # 換算公尺
        weight_kg = float(w_str)

        bmi = weight_kg / (height_m**2)
        bmi = round(bmi, 2)  # 取小數兩位
    
        # 把結果傳回網頁
        return render_template('bmi.html', bmi_result=bmi)

    except ValueError:
        return "❌ 請輸入正確的數字!"

# 4. 定義另一個頁面 (About) - 要放在 app.run 之前！
@app.route('/about')
def about():
    return "<h2>我是 Chun，正在挑戰 7 天全端特訓!!</h2>"

# ==========================================
# 5. 啟動伺服器 (這段是保護罩，最關鍵的一步！)
# ==========================================
if __name__ == '__main__':
    app.run(debug=True)