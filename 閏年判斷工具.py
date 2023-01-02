# 閏年判斷
year=input("請輸入您要判斷的年份(輸入數字即可)：")
year=int(year)
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year}年是閏年")
        elif year%400!=0:
            print(f"{year}年是平年")
        else:
            print("資料有誤")
    elif year%100!=0:
        print(f"{year}年是閏年")
    else:
        print("資料有誤")
elif year%4!=0:
    print(f"{year}年是平年")
else:
    print("資料有誤")
