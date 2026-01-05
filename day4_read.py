import sqlite3

print("=== PDS 會員名單查詢 ===")

conn = sqlite3.connect('pds_system.db')
cursor = conn.cursor()

#1. 執行查詢指令
#SELECT * FROM members: 從 members 表格拿出所有(*)資料
cursor.execute("SELECT * FROM members")

#2. 抓取所有結果 (Fetch All)
# 這會拿到一個 List ，裡面包著很多 Tuple (小元組)
all_members = cursor.fetchall()

print(f"📊目前共有 {len(all_members)}位會員 : ")
print("-------------------")

#3. 用迴圈一個一個印出來
for member in all_members:
    # member 是一個 tuple，例如 ('chun','成功', 1)
    # 記得 : tuple 是用 index (0, 1, 2) 來拿資料，不能用 key
    name = member[0]
    goal = member[1]
    level = member[2]

    print(f"👤 帳號: {name} | 🎯 目標: {goal} | 🆙 等級: {level}")

print("----------------------")
conn.close()
