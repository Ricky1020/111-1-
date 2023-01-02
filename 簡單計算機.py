# 計算機
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
confirm=int(input("請選擇要加減乘除的哪一個？「+」請輸入1，「-」請輸入2，「*」請輸入3，「/」請按4："))
if confirm==1:
    n1=float(input("請輸入被加數："))
    n2=float(input("請輸入加數："))
    equals1=n1+n2
    print(str(n1)+" + "+str(n2)+" = "+str(equals1))
    print("答案是："+str(equals1))
elif confirm==2:
    n3=float(input("請輸入被減數："))
    n4=float(input("請輸入減數："))
    equals2=n3-n4
    print(str(n3)+" - "+str(n4)+" = "+str(equals2))
    print("答案是："+str(equals2))
elif confirm==3:
    n5=float(input("請輸入被乘數："))
    n6=float(input("請輸入乘數："))
    equals3=n5*n6
    print(str(n5)+" * "+str(n6)+" = "+str(equals3))
    print("答案是："+str(equals3))
elif confirm==4:
    n7=float(input("請輸入被除數："))
    n8=float(input("請輸入除數："))
    equals4=n7/n8
    print(str(n7)+" / "+str(n8)+" = "+str(equals4))
    print("答案是："+str(equals4))
else:
    print("資料有誤")
