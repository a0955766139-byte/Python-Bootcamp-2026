# List 是用[]中括號
# Dictionary 是用{}大括號
#格式是 key(標籤): value (內容)

user_profile = {
    "name" : "Chun" , 
    "age" : 18,
    "is_engineer" : True,
    "skills" : ["Python", "Git", "PDS System"], # 字典裡面竟然可以藏 LIST !
    "height" : 160.5
}


#1.建立一個空的字典(準備一本空白筆記本)
reader = {}

print("--- 建立 PDS 讀者檔案 ---")

#2.建一詢問，並直接存入字典(注意看寫法!)
#語法 : 字典名稱['標籤] = 資料

reader ['nickname'] = input("請輸入暱稱 : ")
reader ['goal'] = input("請輸入你的PDS目標 : ")

#這裡我做一個小技巧 : 直接包起來轉成 int 
days_input = input("你預計幾天達成?")
reader['days'] = int(days_input)

#3.讀取資料 (Read)
# 記得! 要從字典拿資料，必須要用reader['標籤"]
print("------------------")
print(f"嗨{reader['nickname']}")
print(f"你的目標是{reader['goal']}, 我們將在{reader['days']}天內一起達成!")