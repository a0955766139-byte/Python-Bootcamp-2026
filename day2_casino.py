import random 
# 這是召喚 Python 的「工具箱」，我們拿出random 這個工具

#1. 產生一個 1 到 6 的隨機整數 (像擲骰子)
dice = random.randint(1, 6)

#2. 產生一個 1 到 100 的隨機整數(像抽獎)
lucky_number = random.randint(1, 100)

print(f"🎲骰子擲出了: {dice}點")
print(f"🎫你的幸運號碼是: {lucky_number}")

#3. 簡單的運氣判斷
if dice == 6:
    print("哇!豹子!你今天的運氣超好!666!")
elif dice >= 4:
    print("是大!運氣不錯喔。")
else:
    print("是小。。。再試一次吧。")





