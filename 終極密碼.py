# 猜數字遊戲
import time
import random
print("歡迎來玩猜數字遊戲")
start=input("請輸入起始範圍：")
start=int(start)
end=input("請輸入結束範圍：")
end=int(end)
ans=random.randrange(start+1,end) # 隨機取整數(含最小值，不含最大值)
a=0
while a==0:
    guess=input(f"請輸入{start}~{end}的數字：")
    guess=int(guess)
    if guess==ans:
        print("恭喜你答對了")
        a=1
    elif guess<ans and guess>start:
        start=guess
        print("加油，快猜到了")
    elif guess>ans and guess<end:
        end=guess
        print("加油，快猜到了")
    else:
        print("資料有誤")
