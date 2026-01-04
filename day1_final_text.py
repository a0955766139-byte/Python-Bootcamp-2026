#1. 讓使用者輸入資料
print("==健康管家 BMI 計算機 ==")
name = input("請問大名:")
birth_year = input("請問出生西元年(例如1990):")
height_str = input("請問身高(cm):")
weight_str = input("請問體重(kg):")

#2. 資料型態轉換與運算
#年齡 : 今年 - 出生年
age = 2026 - int(birth_year)

#身高 : 轉成浮點數(float)並除以100變成公尺
height_str = float(height_str) / 100

#體重 : 轉成浮點數(float), 不用除以100喔!
weight_str = float(weight_str)

#BMI 公式 : 體重 / (身高公尺的平方)
# round(數值， 2 )是為了保留兩位小數，不然數字會太長
bmi = weight_str / (height_str ** 2)
bmi = round(bmi, 2)

#3.輸出結果
print (f"----------------------")
print (f"嗨{name}! 原來你{age}歲了。")
print (f"你的BMI是{bmi}")

#4.健康判斷
if bmi < 18.5:
    print("你太瘦了，需要增重!")
elif bmi >= 18.5 and bmi < 24:
    print("你很健康，繼續保持!")
elif bmi >= 24 and bmi <27:
    print("你輕度肥胖，注意飲食哦!")
elif bmi >=27 and bmi <30:
    print("你中度肥胖，需要運動了!")
else:
    print("你重度肥胖，為了健康要減肥囉!")





