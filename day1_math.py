#1. 讓使用者輸入資料
print("===歡迎來到數學魔法屋===")
name = input("請口大名:")
age_str = input("請問貴庚(請輸入數字)")

#2. 資料型態轉換(關鍵!)
# input() 抓進來的東西永遠是 "文字(String)"，電腦不懂 "文字" 怎麼加減
#所以我們要用 int() 把它變成 "數字(Integer)"
age = int(age_str)

#3. 進行計算
next_year = age +1
decades = age / 10

#4. 輸出結果(f-string 再次登場)
print(f"--------------------------------")
print(f"嗨{name}!原來你{age}歲了。")
print(f"明年這個時候，你就{next_year}歲了!")
print(f"你已經活了{decades}個十年了，真不簡單")



