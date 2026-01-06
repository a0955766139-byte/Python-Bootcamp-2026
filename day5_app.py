from flask import Flask, render_template, request #  引入 render_template
import random

#1. 初始化 Flask 應用程式
# __name__ 代表目前執行的模組
app = Flask(__name__)

#2. 定義路由 (Route)
# 意思是 : 當使用者進入網址 "/" (首頁) 時，執行下面的函式
@app.route('/')
def home():
    #這裡就是 Python 的邏輯層
    user_name = "Chun"
    number = random.randint(1,100) # 產生亂數

    #render_template 會把 HTML 讀進來，並把變數塞進{{}}裡面
    return render_template ('bmi.html')

# 計算路由 : 只接受 POST (表單送出)
@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    #1. 從網頁抓資料 (對應 input 的 name)
    h_str = request.form['height']
    w_str = request.form['weight']

    #2. 進行運算 (記得轉型態)
    try:
        height_m = float(h_str) / 100 #換算公尺
        weight_kg = float(w_str)

        bmi = weight_kg / (height_m**2)
        bmi = round(bmi, 2) # 取小數兩位
    
        #3. 把結果傳回網頁
        return render_template('bmi.html', bmi_result=bmi)

    except ValueError:
        return "❌ 請輸入正確的數字!"

if __name__ == '__main__':
    app.run(debug=True)

#3. 定義另一個頁面
@app.route('/about')
def about():
    return "<h2>我是 Chun，正在挑點戰 7 天全端特訓!!</h2>"

#4. 啟動伺服 (Debug 模式開啟，改程式會自動重整)
if __name__ == '__main__':
    app.run(debug=True)
