import sqlite3

# 這是負責「存」日記的廚師
def save_diary_entry(user_content, user_mood):
    conn = sqlite3.connect('my_journal.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS manifestation_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            mood TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    sql_insert = "INSERT INTO manifestation_log (content, mood) VALUES (?, ?)"
    cursor.execute(sql_insert, (user_content, user_mood))

    conn.commit()
    print("🔥 顯化日記已成功存入資料庫！") # 這行是在終端機看的
    conn.close()

# 這是負責「拿」日記的廚師 (原本你少的就是這個！)
def get_all_diaries():
    conn = sqlite3.connect('my_journal.db')
    cursor = conn.cursor()

    # 選擇所有日記，並依照時間倒序排列 (新的在上面)
    sql_select = "SELECT * FROM manifestation_log ORDER BY created_at DESC"
    cursor.execute(sql_select)

    # 把查到的資料全部打包
    all_logs = cursor.fetchall()
    
    conn.close()
    
    # 🔥 關鍵差異：這裡用 return 把資料「交出去」，而不是用 print 自己印出來
    return all_logs