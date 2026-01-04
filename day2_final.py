import random

#1.建立空清單
options = []

print("🤖PDS決策幫手 : 你有選擇障礙嗎?我來幫你!")
print("請輸入選項 (輸入 'end' 結束):")

while True:
    choice = input("👉加入選項 : ")
    
    if choice == 'end':
        break

    #把選項日入清單
    options.append(choice)
    print(f"  已記錄，目前有{len(options)} 個選項。")

# --- 輸入結束，開始決策---

print("\n 🤔 電腦正在思考中。。。")

#2. 防呆機制 (如果使用者什麼都沒輸入就按end)
if len(options) == 0:
    print("❌ 你沒有輸入任何選項，我無法幫你決定!")

else:
    #3.關鍵功能 : 從清單隨機選一個 (random.choice)
    final_decision = random.choice(options)

    print("-------------------")
    print(f"✨PDS系統建議你現在就去做 : 【{final_decision}】")
    print("-------------------")
    print("加油!立刻去執行!")