import streamlit as st
# 這裡要注意！因為在子資料夾，匯入上一層的檔案有時候會找不到
# 但 Streamlit 很聰明，通常直接 import database_manager 就可以
# 如果報錯，我們再來調整路徑
import database_manager as db

st.set_page_config(page_title="顯化日記", page_icon="📓")

st.title("📓 宇宙顯化日記")
st.write("在這裡，誠實地面對自己，向宇宙下訂單。")

# --- 原本的寫日記表單 (不用再縮放了，因為是獨立頁面，可以大方展開) ---
with st.container():
    st.subheader("✍️ 寫下今天的覺察")
    
    with st.form("diary_page_form", clear_on_submit=True):
        # 這裡版面變大了，我們可以用兩欄排列心情跟內容
        col1, col2 = st.columns([1, 2])
        
        with col1:
            mood = st.selectbox("此刻頻率", ["🥰 超級感恩", "🔥 充滿能量", "😌 平靜放鬆", "😔 需要療癒", "🌟 充滿希望"])
        
        with col2:
            content = st.text_area("顯化內容...", height=150) # 高度可以調高一點
        
        submitted = st.form_submit_button("🚀 發送給宇宙", use_container_width=True) # 按鈕變寬
        
        if submitted and content:
            db.save_diary_entry(content, mood)
            st.success("✨ 接收成功！願望已發送！")
            st.rerun()

# --- 原本的讀取紀錄區 ---
st.divider()
st.subheader("📖 過去的足跡")

logs = db.get_all_diaries()

if not logs:
    st.info("目前還沒有紀錄，快寫下第一篇吧！")
else:
    for row in logs:
        # row[3]時間, row[2]心情, row[1]內容
        with st.expander(f"{row[3][:16]} | {row[2]}"):
            st.write(row[1])