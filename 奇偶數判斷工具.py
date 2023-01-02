# 判斷是奇數或是偶數
number=float(input("請輸入您要判斷的數字："))
if number%2==0:
    number=int(number)
    print(str(number)+"是偶數")
elif number%2==1:
    number=int(number)
    print(str(number)+"是奇數")
else:
    print("資料有誤")
