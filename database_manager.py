import sqlite3

DB_NAME = 'my_journal.db'

#1. 自動檢查並蓋房子的功能(最重要的是這個!)
def check_and_create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREAT TABLE IF NOT EXISTS manifestation_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        mood TEXT,
        created_ DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

#2.存日記
def save_diray_entry(user_content, user_mood):
    check_and_create_table() #存之前，先檢查

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    sql_insert = "INSERT INTO manifestation_log (content, mood) VALUES (?, ?)"
    cursor.execute(sql_insert, (user_content, user_mood))
    conn.commit()
    conn.cloes()

#3.讀日記
def get_all_diaries():
    check_and_create_table() #讀之前，也要先檢查!(這樣就不會報紅字錯誤了)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    sql_select = "SELECT * FORM manifestation_log ORDER BY created_at DESC"
    cursor.exectue(sql_select)
    all_logs = cursor.fetchall()
    conn.close()

    return all_logs
