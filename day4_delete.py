import sqlite3

print("=== PDS 會員移除系統 ===")

conn = sqlite3.connect('pds_system.db')
cursor = conn.cursor()

# 1. 顯示名單
cursor.execute("SELECT * FROM members")
all_members = cursor.fetchall()
# 使用 List Comprehension 取出名字，方便閱讀
print(f"目前名單: {[m[0] for m in all_members]}")

# 2. 詢問
target_name = input("請問你要移除哪位會員的帳號? ")

# 3. 執行刪除 (這行最重要！)
# 翻譯：從 members 表格刪除，條件是 name 等於「?」
sql = "DELETE FROM members WHERE name = ?"

# 執行時，把 target_name 填入那個 ?
cursor.execute(sql, (target_name,))

if cursor.rowcount > 0:
    conn.commit()
    print(f"🗑️ 成功！會員 '{target_name}' 已從資料庫移除。")
else:
    print(f"⚠️ 找不到 '{target_name}' 這個人，刪除失敗。")

conn.close()