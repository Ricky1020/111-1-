# 抽籤
import random
print("這是抽籤程式")
start=input("請輸入起始範圍：")
start=int(start)
end=input("請輸入結束範圍：")
end=int(end)
times=input("請輸入抽籤的次數：")
times=int(times)
numbers=[]
for i in range(times):
    number=random.randrange(start,end) # 隨機取整數(含最小值，不含最大值)
    numbers.append(number)
print(numbers)
