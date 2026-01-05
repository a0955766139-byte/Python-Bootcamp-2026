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

#1. 讀取資料(Read)
#不用算第幾個，直接呼叫標籤的名字
print(f"姓名: {user_profile['name']}")
#2.修改資料 (Update)
#假設過了一年，長高了，也變老了
user_profile['age'] = 19
user_profile['height'] = 161.0
print(" --- 過了一年後 ---")
print(f"現在{user_profile['age']}歲，身高{user_profile['height']}cm")

#3. 新增資料 (Create)
# 直接寫一個不存在的標籤，就會自動新增!
user_profile['city'] = "Taipei"
print (f"居住城市: {user_profile['city']}")

#4.刪除資料(Delete)
del user_profile['is_engineer']
#刪除後如果去印它，程式會報錯喔!
print ("已刪除工程師身份標籤")