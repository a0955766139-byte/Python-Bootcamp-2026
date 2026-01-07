import sqlite3

DB_NAME = 'my_journal.db'

# 1. 抽離出一個專門用來「確保資料庫與表格存在」的工具人函式
def check_and_create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS manifestation_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            mood TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# 2. 存日記的功能
def save_diary_entry(user_content, user_mood):
    check_and_create_table() # 🔥 寫入前，先檢查表格在不在
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    sql_insert = "INSERT INTO manifestation_log (content, mood) VALUES (?, ?)"
    cursor.execute(sql_insert, (user_content, user_mood))
    conn.commit()
    conn.close()

# 3. 讀日記的功能
def get_all_diaries():
    check_and_create_table() # 🔥 重點在這裡！讀取前，也要先檢查表格在不在！
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    sql_select = "SELECT * FROM manifestation_log ORDER BY created_at DESC"
    cursor.execute(sql_select)
    all_logs = cursor.fetchall()
    conn.close()
    
    return all_logs