name = str(input())
studentID = int(input())
Chinese = int(input())
CS = int(input())
PD = int(input())

Total = Chinese + CS + PD
A = Total//3

"""
可使用1)"字串..."+變數名稱（備注：如果是數字需在前面加str，將數字改爲字串）
      2）f"字串.....{變數名稱}"
"""
print( "\nName:" +name)
print("ID:"+str(studentID))
print("Average:"+str(A))
print(f'Total:{Total}')
