#1.建立一個空的清單(像一個空的購物籃)
#中括號[]代表這是一個 List
shopping_list = []

print("🛒歡迎使用智慧購物清單!")
print("輸入'q'或'quit'可以結束並列印清單。")

while True:
    #2.讓使用者輸入
    item = input("請輸入想買的物品")

    #3.檢查是否要離開(如果輸入 q 就打破迴圈)
    if item == 'q' or item == 'quit':
        break

    #4.把物品丟進清單(append是附加、加入的意思)
    #這行是關鍵!把 item 塞進 shoppint_list 這個背包裡
    shopping_list.append(item)

    #len()可以計算清單裡面目前有幾個東西
    print(f"✅ 已加入:{item}(目前背包有{len(shopping_list)}樣東西)")

    # ---迴圈結束後(break 跳到這裡)

    print("\n======最終購物清單======")

    #5. For 迴圈 : 專門用來「遍歷」清單
    #翻譯：對於(for) 清單(shopping_list) 裡的 每一個東西(thing)
    #電腦會自動一個一個拿出來，直到拿完為止
    for thing in shopping_list:
        print(f"👉待買:{thing}")

    print ("==================")
    print (f"總共要買{len(shopping_list)}項物品。")