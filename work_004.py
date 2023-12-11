#project = BMI calculation
#20230919

height = float(input())
weight = int(input())

BMI = weight/height**2

# 四舍六入五看偶
#找出保留數后一位的數值
a = int(BMI*1000)
b = int((BMI*1000//10)*10)

# int的原因是擔心減法時會有細微誤差（2-1=1.0000003）
if int(a-b) == 5:
    if int(BMI * 100) % 2 == 0: #當保留數后一位為5時，判斷保留數是否為偶數
        BMI -= 0.001
    else:
        BMI += 0.001          

print(format(BMI, '.2f')) 
