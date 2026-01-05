#1. 引入 json 工具箱(New!)
import json
import os #檢查檔案用


# 建立一個空的「資料庫」(其實就是一個 List)
pds_database = []

#--- 讀取舊資料(讓程式有記憶)(New!)---
if os.path.exists('pds_data.json'):
    with open('pds_data.json', 'r', encoding='utf-8') as f:
        pds_database = json.load(f)
    print(f"📂發現舊檔案!已載入{len(pds_database)}筆資。")
else:
    print("📂找不到舊檔案，建立新資料庫。")

print("=== 歡迎來到 PDS 會員系統 ===")

while True:
    print("\n--- 新增會員 (輸入'q' 結束) ---")
    name = input("請輸入姓名 : ")

    if name == 'q' :
        break

    goal = input("請輸入目標 : ")

    member = {
        "name" : name,
        "goal" : goal,
        "status": "Active"
    }
    
    pds_database.append(member)
    print(f"✅會員 {name}已暫存。")

# --- 迴圈結束後，把資料寫入硬碟(New!) ---

print("\n💾 正在存檔中。。。")
# 'W' 代表寫入(write), ensure_ascii=False是為了讓中文正常顯示
with open('pds_data.json','w', encoding='utf-8') as f:
    json.dump(pds_database, f, ensure_ascii=False, indent=4)

print("✅存檔完成!檔案名稱 : pds_data.json")

print("\n===============")
print(f"📊PDS 系統總報表 (共 {len(pds_database)}人)")

print("=== 歡迎來到 PDS 會員系統 ===")

while True:
    print("\n --- 新增會員 (輸入 'q' 結束)--- ")
    name = input ("請輸入姓名 : ")
    
    #.strip() 去除前後空白
    #.lower() 把大寫 Q 變成小寫 q
    if name.strip().lower() =='q' :
    
        break
    goal = input ("請輸入目標 : ")

    #2. 建立一張「會員卡」 (Dictionary)
    # 每次迴圈跑這行，都會產生一個美新的字典
    member = {
        "name" : name,
        "goal" : goal,
        "status" : "Active"  #預設每個會員都是活躍中
    }

    #3.把這張卡片丟進卡片裡 (List)
    pds_database.append(member)
    print(f"✅會員 {name}已存檔!目前共有 {len(pds_database)}人。")

    #  ---輸入結束，列印報表 ---

    print("\n ======================")
    print(f"📊 PDS 系統總報表 (共 {len(pds_database)}人)")
    print("=========================")

    #4. 遍歷資料庫 (這段邏輯稍微難一點，請仔細看)
    # user 變數在每次迴圈中，都會變成期中一個字典
for user in pds_database:
    #這裡的 user 就是上面存進去的 member
    print(f"👤姓名: {user['name']}")
    print(f"  目標: {user['goal']}")
    print(f"  狀態: {user['status']}")
    print("--------------------")