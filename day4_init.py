import sqlite3 # Python 內建的 SQL 工具

#1. 連接資料庫 (如果檔案不存在，它會自動建立!)
#這就像打開一個 Excel 檔
conn = sqlite3.connect('pds_system.db')

#2. 建立「遊標 (Cursor)」
# 想像這是一隻拿著筆的手，準備要寫字
cursor = conn.cursor()

#3. 撰寫 SQL 指令 (這是通用的 SQL 語法，不是 Python 喔!)
#CREATE TABLE : 建立表格
#IF NOT EXISTS : 如果已經有了就不要再重複建
#PRIMARY KEY : 主鍵 (email)，保證 "name"絕對不能重複!
sql_command = """
CREATE TABLE IF NOT EXISTS members (
    name TEXT PRIMARY KEY,
    goal TEXT,
    level INTEGER
);
"""

#4. 執行指令
cursor.execute(sql_command)

#5. 確認存檔 (Commit)
conn.commit()

#6. 關閉連線 (養成好習慣)
conn.close()

print("✅ 資料庫與表格 'members' 已建立完成!")