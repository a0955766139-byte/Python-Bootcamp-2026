#1. 讓使用者輸入資料

name = input("請問大名:")
birth_year = input("請問出生西元年(例如1990):")
height_str = input("請問身高(公分):")
weight_str = input("請問體重(公斤):")
   

#2. 資料型態轉換(關鍵!)
# input() 抓進來的東西永遠是 "文字(String)"，電腦不懂 "文字" 怎麼加減
#所以我們要用 int() 把它變成 "數字(Integer)"
age = 2026 - int(birth_year)
height_str = int(height_str) / 100
weight_str = int(weight_str) 
bmi = int(weight_str / ( height_str ** 2))

#4. 輸出結果(f-string 再次登場)
print(f"--------------------------------")
print(f"嗨{name}!原來你{age}歲了。")
print(f"你的BMI是{bmi}")

if bmi < 18.5:
    print("你太瘦了，需要增重")
elif bmi >= 18.5 and bmi < 24:
    print("你很健康，繼續保持")
elif bmi >= 24 and bmi < 27:
    print("你輕度肥胖，需要減肥")
elif bmi >= 27 and bmi < 30:
    print("你中度肥胖，需要減肥")
else:
    print("你重度肥胖，需要減肥")
