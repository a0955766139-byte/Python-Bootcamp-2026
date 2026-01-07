import streamlit as st
import pandas as pd
import numpy as np

#--- 1. 設定網頁配置 (這行要擺第一行) ---
st.set_page_config(page_title="喬鈞心學", page_icon="🔮")

#--- 2. 標題區塊 ---
st.title("喬鈞文化·喬鈞心學 🔮")
st.caption("歡迎回到喬鈞心學，練習覺察與顯化的日常。")

#---3. 每日提醒(模疑照片中的通知區) ---
with st.expander("🔔 今日提醒 (點擊展開)", expanded=True):
    st.info("API 已連線成功，可以開始使用六大主功能。")
    st.write("🌟 今日宇訊息 : 相信你的直覺，財富正在靠近!")

st.divider() #畫一條分隔線

# --- 4. 核心功能區(使用Columns 做 2x3 的網格排版) ---
# 建立兩欄 (col1, col2)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🃏 每日抽牌")
    st.write("用一張牌看見當下訊息")
    if st.button("開始抽牌"):
        st.toast("抽牌功能開發中...🔮")

with col2:
    st.subheader("🔢 數字心理學")
    st.write("生命靈數 x 現代心理學")
    if st.button("查看命盤"):
        st.toast("命盤載入中...📊")

st.write("---") # 分隔距

col3, col4 = st.columns(2)

with col3:
    st.subheader("📓 顯化日記")
    st.write("寫下今天的覺察與顯化")
    if st.button("寫日記"):
        st.toast("開啟日記本 ✍️")

with col4:
    st.subheader("🎧 個案 & 課程")
    st.write("一對一解析與進階課程")
    if st.button("預約諮詢"):
        st.link_button("前往預約", "https://calendar.google.com") # 範例連結

st.write("---") # 分隔距

col5, col6 = st.columns(2)

with col5:
    st.subheader("🛒 商城")
    st.write("書籍、課程、數字工具")
    st.button("前往商城")

with col6:
    st.subheader("👤 會員中心")
    st.write("個人資料 & 設定")
    st.button("管理帳戶")

# --- 5. Day 9 重點：數據視覺化 (Data Visualization) ---
st.divider()
st.header("📊 本週能量趨勢 (Day 9 練習)")
st.write("這是你本週的「覺察指數」與「顯化進度」：")

# 這裡我們用 Python 畫一個簡單的折線圖
chart_data = pd.DataFrame(
    np.random.randn(7, 2) + [10, 5],  # 隨機產生數據模擬
    columns=['覺察指數', '顯化能量']
)

# Streamlit 畫圖只需一行指令！
st.line_chart(chart_data)

st.caption("小提示：試著把滑鼠移到圖表上，可以看到詳細數字喔！")