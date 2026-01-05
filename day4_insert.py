import sqlite3

print("=== PDS 會員註冊系統(SQL版) ===")

name_input = input("請輸入帳號 (Name): ")
goal_input = input("請輸入目標 (Goal): ")


#1. 連線
conn = sqlite3.connect('pds_system.db')
cursor = conn.cursor()

try:
    #2. 執行 SQL 新增指令
    #INSERT INTO 表格 (欄位1, 欄位2...)
    sql = "INSERT INTO members (name, goal, level) VALUES (?, ?, ?)"

    #3. 把資料填進去 (預設 level 為 1)
    cursor.execute(sql, (name_input, goal_input, 1))

    conn.commit()
    print(f"🎉 註冊成功 ! 歡迎 {name_input}加入。")

except sqlite3.IntegrityError:
    #4. 捕捉「重複註冊」的錯誤
    #因為我們設定 name 是PRIMARY KEY，重複 SQL 會報錯
    print(f"❌ 錯誤 : 帳號'{name_input}'已經存在了!不能重複註冊。")

finally:
    #不管成功失則，最後都要關閉連線
    conn.close()