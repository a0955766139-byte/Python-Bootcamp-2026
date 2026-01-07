import sqlite3


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

    # 🔥 修正點在這裡：是 VALUES (記得加 S，不要拼錯囉)
    sql_insert = "INSERT INTO manifestation_log (content, mood) VALUES (?, ?)"
    
    cursor.execute(sql_insert, (user_content, user_mood))

    conn.commit()
    print("🔥 顯化日記已成功存入資料庫！")
    conn.close()

# --- 測試區 ---
#diary_text = "今天我練習了感恩冥想，感覺宇宙都在幫我！"
#current_mood = "Super Happy"
#save_diary_entry(diary_text, current_mood)

#呼叫函式儲存
#save_diary_entry(diary_text, current_mood)

def show_all_diaries():
    #1. 一樣先連線
    conn = sqlite3.connect('my_journal.db')
    cursor = conn.cursor()

    #2. 執行「加喚術」(查詢指令)
    #我們要把所有的日記找出來，並且最新的排最前面
    sql_select = "SELECT * FROM manifestation_log ORDER BY created_at DESC"
    cursor.execute(sql_select)

    #3.抓取結果 (Fetch)
    #fetchall()意思就是「把剛剛查到的東西全部打包帶回來」
    all_logs = cursor.fetchall()

    #4. 顯示在畫面上(這裡先用 Print 顯示在終端機)
    print("\n📖 --- 我的顯化日記本 --- 📖")

    if not all_logs:
        print("目前還沒有日記喔，快去寫一篇吧!")
    else:
        for row in all_logs:
            #row 是一個tuple (元組)，裡面的順序對應資料庫欄位
            #row[0] 是 id (編號)
            #row[1] 是content (內容)
            #row[2] 是mood (心情)
            #row[3] 是time (時間)

            print(f"{row[3]} 心情: {row[2]}")
            print(f"日記 : {row[1]}")
            print("_" * 30) #畫一條分隔線

    #5. 關閉連線 (讀取完畢就可以關了)
    conn.close()

# --- 測試看看 ---
# 呼叫這個函式
show_all_diaries()
