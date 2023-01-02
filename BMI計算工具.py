# BMI計算
height1=float(input("請輸入您的身高(公分)："))
height=height1/100
weight=float(input("請輸入您的體重(公斤)："))
bmi=weight/(height**2)
if bmi<18.5:  
    print("您的BMI值是："+str(bmi)+"，過輕")
elif bmi>24:
    print("您的BMI值是："+str(bmi)+"，過胖")
else:
    print("您的BMI值是："+str(bmi)+"，正常")
